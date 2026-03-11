# ДЗ 25 - Мониторинг и логирование

В проекте есть:
- `docker-compose.yaml`
- `.env`
- `configs/prometheus.yml`
- `mlapp/server.py` с `starlette-exporter`
- полный FastAPI ML сервис для проверки метрик
- `node-exporter` в docker-compose

## Запуск

```bash
docker compose up --build
```

После запуска будут доступны:
- ML service: `http://localhost:8000`
- Metrics: `http://localhost:8000/metrics`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`
- Node Exporter: `http://localhost:9100/metrics`

## Как добавить Prometheus в Grafana

1. Открыть Grafana.
2. Войти под логином и паролем из `.env`.
3. Добавить data source типа Prometheus.
4. Указать URL: `http://prometheus:9090` внутри docker-сети
   или `http://localhost:9090` при открытии из браузера.

## Панели для дашборда

Количество запросов `query_range` в Prometheus:
```promql
increase(prometheus_http_requests_total{handler="/api/v1/query_range"}[1m])
```

Загрузка CPU через node-exporter:
```promql
avg by (mode) (rate(node_cpu_seconds_total[1m]))
```

Пример полезной метрики для ML сервиса:
```promql
sum(rate(starlette_requests_total{app_name="diabets_ml_service", method="POST", path="/api/v1/predict"}[1m]))
```

## Пример запроса в ML сервис

```bash
curl -X POST http://127.0.0.1:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 59.0,
    "sex": 2.0,
    "bmi": 32.1,
    "bp": 101.0,
    "s1": 157.0,
    "s2": 93.2,
    "s3": 38.0,
    "s4": 4.0,
    "s5": 4.8598,
    "s6": 87.0
  }'
```
