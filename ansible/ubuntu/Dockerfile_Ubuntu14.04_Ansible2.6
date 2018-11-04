# Based on Ubuntu 14.04
FROM ubuntu:14.04
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
    libssl-dev \
    libffi-dev \
    python-pip \
    python-dev \
 && apt-get autoremove \
 && apt-get clean


RUN git clone --recursive -b stable-2.6 https://github.com/ansible/ansible \
 && cd ./ansible \
 && pip install --upgrade packaging \
 && pip install --upgrade setuptools \
 && pip install --upgrade -r ./requirements.txt \
 && make \
 && make install \
 && cd .. \
 && rm -rf ansible
