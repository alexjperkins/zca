FROM python:3.8-slim-buster
MAINTAINER Alex Perkins

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

### --- Requirements --- ###
RUN apt-get update \
	&& apt-get install -y build-essential \
	&& apt-get install -y  libpq-dev \
	&& apt-get purge -y --auto-remove -o API::AutoRemove::RecommendsImportant=false \
	&& rm -rf  /var/lib/apt/lists/*

COPY ./requirements/ /requirements
RUN pip install -r /requirements/development.txt


### --- Command Setup --- ###
COPY ./compose/local/zca/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/zca/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


### --- Path Setup --- ###
WORKDIR /zca
ENV PYTHONPATH=/:/zca:/tests


### --- Entrypoint --- ###
ENTRYPOINT ["/entrypoint"]
