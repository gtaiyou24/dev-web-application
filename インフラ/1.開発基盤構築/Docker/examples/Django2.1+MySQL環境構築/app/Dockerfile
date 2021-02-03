FROM python:3


RUN mkdir -p /home/app
WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER true

RUN apt-get update
RUN apt-get install -y mysql-client vim
ADD ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt