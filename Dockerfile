FROM python:3.12 AS builder
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /app
COPY pyproject.toml ./
RUN poetry install --no-dev


FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app ./
COPY . .
