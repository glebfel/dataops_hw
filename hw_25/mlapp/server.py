import os
from functools import lru_cache

import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from starlette_exporter import PrometheusMiddleware, handle_metrics


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


@lru_cache
def load_model():
    return joblib.load(os.getenv("LOCAL_MODEL_PATH", "model/diabets_model.joblib"))


app = FastAPI(title="Diabets ML service", version="1.1.0")

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
    model = load_model()
    row = [[
        payload.age,
        payload.sex,
        payload.bmi,
        payload.bp,
        payload.s1,
        payload.s2,
        payload.s3,
        payload.s4,
        payload.s5,
        payload.s6,
    ]]
    result = float(model.predict(row)[0])
    return PredictResponse(predict=round(result, 2))
