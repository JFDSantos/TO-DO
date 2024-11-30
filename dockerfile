# Usar uma imagem oficial do Python como base
FROM python:3.10-slim AS base

WORKDIR /app

EXPOSE 8000

FROM python:3.10-slim AS build

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM base AS final

COPY --from=build /src /app

ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
