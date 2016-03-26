# Based on Ubuntu 14.04
FROM ubuntu:14.04
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -q -y \
    apt-utils \
    wget \
    nano \
    git

RUN apt-get update && \
    apt-get install -q -y \
    python-pip \
    python-dev \
    python-yaml \
    python-jinja2   

RUN pip install ansible


