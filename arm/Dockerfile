# Based on gmauro/ansible
FROM gmauro/ansible
MAINTAINER Gianmauro Cuccuru <gmauro@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN git clone http://github.com/gmauro/arm.git /tmp/arm
WORKDIR /tmp/arm
RUN ansible-playbook container.yml
