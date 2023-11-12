FROM python:3.10-slim

RUN mkdir backend

WORKDIR /backend/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
