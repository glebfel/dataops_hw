# ДЗ 13 — Введение в Kubernetes (Вариант 1)

Артефакты:
- deployment.yaml
- service.yaml
- ingress.yaml

## Применение
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

## Проверка
```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

### CURL (пример для Ingress NGINX)
Убедитесь, что Ingress Controller установлен, и у вас есть IP/адрес ingress.
Для kind обычно используют порт-маппинг или LB, для minikube: `minikube tunnel`.

```bash
curl -H "Host: example.com" http://<INGRESS_IP>/
```
