FROM python:3.9.7-slim-buster

ARG UID=1000
ARG GID=1000
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libpq-dev \
    build-essential

RUN pip install poetry

RUN addgroup --gid $GID app
RUN adduser --disabled-password --gecos '' --uid $UID --gid $GID app

RUN mkdir /app
RUN chown -R app /app

USER app

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-interaction
