FROM python:3.14-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends nodejs npm && \
    npm install -g configurable-http-proxy && \
    pip install --no-cache-dir jupyterhub jupyterlab notebook && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/jupyterhub
COPY jupyterhub_config.py .

EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]