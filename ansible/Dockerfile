# Based on Debian Wheezy
FROM debian:wheezy
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -q -y \
    apt-utils 

RUN apt-get update && \
    apt-get install -q -y \
    python-pip \
    python-dev \
    python-yaml    

RUN pip install ansible