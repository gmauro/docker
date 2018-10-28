# Based on Debian
FROM debian:8
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -q -y \
    apt-utils \
    wget \
    nano \
    git \
    build-essential \
    python-pip \
    python-dev \
    python-yaml \
    python-paramiko \
    python-six \
    python-httplib2 \
    python-jinja2 \  
 && apt-get autoremove \
 && apt-get clean


RUN git clone --recursive -b stable-2.6 https://github.com/ansible/ansible \
 && cd ./ansible \
 && make install \
 && cd .. \
 && rm -rf ansible
