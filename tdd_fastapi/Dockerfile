FROM python:3.9.2-slim-buster

# Definimos nuestro directorio donde estaremos
# aplicando los comandos
WORKDIR /usr/src/app

# Colocamos las siguientes variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .