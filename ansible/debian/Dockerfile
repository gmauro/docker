# Based on Debian
FROM debian:8
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -q -y \
    apt-utils \
    wget \
    nano \
    git \
    python-pip \
    python-dev \
    python-yaml \
    python-jinja2 \
 && apt-get autoremove \
 && apt-get clean

RUN pip install ansible