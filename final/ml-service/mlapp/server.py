import json
import logging
import os
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from functools import lru_cache

import joblib
import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel
from starlette_exporter import PrometheusMiddleware, handle_metrics


logger = logging.getLogger("ml_service")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)

MODEL_VERSION = "1.0.0"


def _log_json(event: str, **kwargs):
    record = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **kwargs}
    logger.info(json.dumps(record))



def _get_db_conn():
    dsn = os.getenv("LOG_DATABASE_URI")
    if not dsn:
        return None
    return psycopg2.connect(dsn)


def _ensure_log_table():
    conn = _get_db_conn()
    if conn is None:
        return
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS prediction_log (
                    id SERIAL PRIMARY KEY,
                    ts TIMESTAMPTZ DEFAULT now(),
                    model_version TEXT,
                    input JSONB,
                    output DOUBLE PRECISION,
                    duration_ms DOUBLE PRECISION
                )
            """)
    conn.close()


def _log_to_db(input_data: dict, output: float, duration_ms: float):
    conn = _get_db_conn()
    if conn is None:
        return
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO prediction_log (model_version, input, output, duration_ms) VALUES (%s, %s, %s, %s)",
                    (MODEL_VERSION, json.dumps(input_data), output, duration_ms),
                )
        conn.close()
    except Exception as e:
        _log_json("db_log_error", error=str(e))



@lru_cache
def load_model():
    return joblib.load(os.getenv("LOCAL_MODEL_PATH", "model/diabets_model.joblib"))



class PatientFeatures(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float


class PredictResponse(BaseModel):
    predict: float
    model_version: str = MODEL_VERSION



@asynccontextmanager
async def lifespan(application: FastAPI):
    _ensure_log_table()
    load_model()
    _log_json("service_started", model_version=MODEL_VERSION)
    yield


app = FastAPI(title="Diabetes ML Service", version=MODEL_VERSION, lifespan=lifespan)

app.add_middleware(
    PrometheusMiddleware,
    app_name="diabets_ml_service",
    group_paths=True,
    prefix="ml_service",
)
app.add_route("/metrics", handle_metrics)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/v1/predict", response_model=PredictResponse)
def predict(payload: PatientFeatures) -> PredictResponse:
    _log_json("predict_request", input=payload.model_dump())
    start = time.time()

    model = load_model()
    row = [[payload.age, payload.sex, payload.bmi, payload.bp,
            payload.s1, payload.s2, payload.s3, payload.s4,
            payload.s5, payload.s6]]
    result = round(float(model.predict(row)[0]), 2)

    duration_ms = (time.time() - start) * 1000
    _log_json("predict_response", output=result, duration_ms=round(duration_ms, 2), model_version=MODEL_VERSION)
    _log_to_db(payload.model_dump(), result, duration_ms)

    return PredictResponse(predict=result)
