# Based on Ubuntu 14.04
FROM ubuntu:14.04
MAINTAINER Gianmauro Cuccuru <gmauro@gmail.com> 

ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get update && \
    apt-get install -q -y \
    apt-utils \
    wget \
    nano \
    git \
    supervisor

RUN apt-get install -y openssh-server

RUN mkdir -p /var/log/supervisor /var/run/sshd

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]