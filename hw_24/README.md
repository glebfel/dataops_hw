# ДЗ 24 — Полноценный ML-сервис

## Содержимое
- `research/train.ipynb`
- `mlapp/server.py`
- `mlapp/__main__.py`
- `model/diabets_model.joblib`
- `Dockerfile`
- `docker-compose.yaml`
- `curl_examples.txt`

## Локальный запуск
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m mlapp
```

## Docker
```bash
docker compose up --build
```
