FROM python:3.9.4 as builder

WORKDIR /app/backend/

RUN pip install poetry

ADD pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt

FROM python:3.9.4

ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend/

COPY --from=builder /app/backend/requirements.txt .

RUN pip install -r requirements.txt

ADD . .
