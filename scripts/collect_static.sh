#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

export DJANGO_CACHE_TIMEOUT=100
export DJANGO_SECRET_KEY=FAKE_KEY
export DJANGO_SETTINGS_MODULE=config.production_settings

cd $root/django/

py manage.py collectstatic

# setting nginx
COPY nginx/mymdb.conf /etc/nginx/sites-available/mymdb.conf
RUN rm/etc/nginx/sites-enabled/*
RUN ln -s /etc/nginx/sites-available/mymdb.conf /etc/nginx/sites-enabled/mymdb.conf

COPY runit/nginx /etc/service/nginx
RUN chmod +x /etc/service/nginx/run
