# ДЗ 15 — Helm

Содержимое:
- nginx-chart/ (Helm chart)
- values-small.yaml (пример: поменять tag и включить resources)
- values-no-ingress.yaml (пример: отключить ingress)

## Быстрый старт
```bash
cd nginx-chart
helm install my-nginx .
```

## Варианты деплоя (несколько раз с разными values)
```bash
# 1) дефолт
helm install nginx-a ./nginx-chart

# 2) другой tag + resources
helm install nginx-b ./nginx-chart -f values-small.yaml

# 3) без ingress
helm install nginx-c ./nginx-chart -f values-no-ingress.yaml
```

## Обновление (пример)
```bash
helm upgrade nginx-b ./nginx-chart -f values-small.yaml
```

## Удаление
```bash
helm uninstall nginx-a nginx-b nginx-c
```
