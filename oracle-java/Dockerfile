# Based on Debian Jessie
FROM debian:jessie
MAINTAINER Gianmauro Cuccuru <gmauro@crs4.it>

ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \
    | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \
    | tee -a /etc/apt/sources.list.d/webupd8team-java.list

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
     --recv-keys EEA14886

RUN apt-get update \
    &&  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select \
    true | /usr/bin/debconf-set-selections \
    && apt-get install -y oracle-java8-installer
