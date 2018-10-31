# Based on Ubuntu 16.04
FROM ubuntu:16.04
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get install -q -y \
    apt-utils \
    apt-transport-https \
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
 && pip install -r ./requirements.txt \
 && pip install packaging \
 && make \
 && make install \
 && cd .. \
 && rm -rf ansible
