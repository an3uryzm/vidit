FROM python:3.10.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl libpq-dev build-essential python-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --system --group app
WORKDIR /app

COPY --chown=app:app requirements.txt .
RUN python -m pip install --no-cache-dir --disable-pip-version-check --requirement requirements.txt

USER app
COPY --chown=app:app . .