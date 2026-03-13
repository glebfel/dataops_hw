FROM python:3.11-slim

RUN pip install --no-cache-dir mlflow psycopg2-binary

EXPOSE 5000

CMD ["mlflow", "server", \
     "--host", "0.0.0.0", \
     "--port", "5000", \
     "--backend-store-uri", "postgresql://mlflow:mlflow_pass@db:5432/mlflow", \
     "--default-artifact-root", "/mlflow/artifacts"]