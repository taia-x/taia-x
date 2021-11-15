FROM python:3.9.7

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY . /backend

RUN apt-get update \
    && apt-get clean

ENTRYPOINT [ "./docker-start.sh" ]