FROM python:3.11

RUN mkdir backend

WORKDIR /backend/

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .