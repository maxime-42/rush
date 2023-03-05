FROM python:3.10.10-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
