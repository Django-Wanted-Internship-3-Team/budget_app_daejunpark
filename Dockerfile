FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.6.1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN mkdir /app/
RUN mkdir /app/src/
WORKDIR /app

COPY pyproject.toml /app/
COPY setup.cfg /app/

RUN pip install poetry==${POETRY_VERSION}
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
