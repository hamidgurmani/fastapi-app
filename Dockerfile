# ----Builder stage---
FROM python:3.10-slim AS builder

WORKDIR /install

COPY app/requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir --prefix=/install  -r requirements.txt

# ----- Run stage ----

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*  

COPY --from=builder /install /usr/local

COPY app /app/app

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN useradd -m appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /data

USER appuser


ENTRYPOINT ["/entrypoint.sh"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


