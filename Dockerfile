FROM python:3.12 AS builder
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:${PATH}"
ENV PYTHONPATH="/app"
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main


#FROM python:3.12-slim
#WORKDIR /app
#COPY --from=builder /app ./


