# Based on Debian latest
FROM debian:latest
MAINTAINER Gianmauro Cuccuru <gmauro@gmail.com> 

ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get update && \
    apt-get install -q -y \
    apt-utils \
    wget \
    nano \
    git

RUN apt-get install -y openssh-server

RUN mkdir -p /var/run/sshd

ADD supervisord.conf /etc/supervisor/conf.d/sshd.conf

EXPOSE 22
