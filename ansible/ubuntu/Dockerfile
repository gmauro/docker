# Based on gmauro/ubuntu
FROM gmauro/ubuntu
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -q -y \
    python-pip \
    python-dev \
    python-yaml \
    python-jinja2   

RUN pip install ansible
