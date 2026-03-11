FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mlapp ./mlapp
COPY model ./model

EXPOSE 8000

CMD ["python", "-m", "mlapp"]
