# ДЗ 14 — k8s ресурсы (Вариант 1)

Артефакты:
- nginx/deployment.yaml (ресурсы + /dev/shm=128Mi)
- nginx/service.yaml (без изменений относительно ДЗ13)
- nginx/ingress.yaml (без изменений относительно ДЗ13)
- redis/deployment.yaml
- redis/service.yaml

## Применение
```bash
kubectl apply -f nginx/deployment.yaml
kubectl apply -f nginx/service.yaml
kubectl apply -f nginx/ingress.yaml

kubectl apply -f redis/deployment.yaml
kubectl apply -f redis/service.yaml
```

## Самопроверка
```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

> Для подтверждения /dev/shm можно зайти в pod nginx и проверить размер:
```bash
kubectl exec -it deploy/nginx -- df -h /dev/shm
```
