FROM ubuntu:18.04 AS djample_base

RUN useradd www --create-home --shell /bin/bash
WORKDIR /home/www

RUN set -x; \
  apt-get update -y &&\
  apt-get install -y cron &&\
  apt-get install -y python3.6 python3-pip python3.6-venv &&\
  apt-get install -y postgresql-client &&\
  apt-get install -y libpcre3 libpcre3-dev &&\
  /usr/bin/python3.6 -m venv venv/ &&\
  chown www:www -R venv/