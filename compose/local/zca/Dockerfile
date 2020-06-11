FROM python:3.8-slim-buster
MAINTAINER Alex Perkins

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
	&& apt-get install -y build-essential \
	&& apt-get install -y  libpq-dev \
	&& apt-get purge -y --auto-remove -o API::AutoRemove::RecommendsImportant=false \
	&& rm -rf  /var/lib/apt/lists/*

COPY ./requirements/ /requirements
RUN pip install -r /requirements/development.txt
