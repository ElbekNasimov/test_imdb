FROM phusion/baseimage

# add code and directories
RUN mkdir/test_imdb
WORKDIR /test_imdb
COPY requirements* /test_mymdb/
COPY django/ /test_imdb/django
COPY scripts/ /test_imdb/scripts
RUN mkdir /var/log/mymdb/
RUN touch /var/log/mymdb/mymdb.log

RUN apt-get -y update
RUN apt-get install -y \
    nginx \
    postgresql-client \
    python3 \
    python-pip
RUN pip3 install virtualenv
RUN virtualenv /test_imdb/venv
RUN bash /test_imdb/scripts/pip_install.sh /test_mymdb

# collect the static files
RUN bash /test_imdb/scripts/collect_static.sh /test_mymdb

# configure uwsgi
COPY uwsgi/mymdb.ini /etc/uwsgi/apps-enabled/mymdb.ini
RUN mkdir -p /var/log/uwsgi/
RUN touch /var/log/uwsgi/mymdb.log
RUN chown www-data /var/log/uwsgi/mymdb.log
RUN chown www-data /var/log/mymdb/mymdb.log

COPY runit/uwsgi /etc/service/uwsgi
RUN chmod +x /etc/service/uwsgi/run

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp*

EXPOSE 80
