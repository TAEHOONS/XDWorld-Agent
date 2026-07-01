FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./app
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

EXPOSE 8000

CMD ["sh", "-c", "gunicorn app.main:app --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker --log-level=info --access-logfile - --error-logfile - --capture-output --timeout ${GUNICORN_TIMEOUT:-1800} --graceful-timeout ${GUNICORN_GRACEFUL_TIMEOUT:-300} --keep-alive ${GUNICORN_KEEPALIVE:-300} --workers ${GUNICORN_WORKERS:-2} --worker-connections ${GUNICORN_WORKER_CONNECTIONS:-1000} --max-requests ${GUNICORN_MAX_REQUESTS:-0} --max-requests-jitter ${GUNICORN_MAX_REQUESTS_JITTER:-0}"]
