# Based on gmauro/ansible
FROM gmauro/ansible
MAINTAINER Gianmauro Cuccuru <gmauro@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN git clone https://github.com/gmauro/irods-in_place /tmp/irods-in_place
WORKDIR /tmp/irods-in_place
RUN ansible-playbook container.yml
