FROM python:3
RUN apt update && apt install -y mysql-client && \
    pip3 install django requests mysqlclient
COPY . /srv
WORKDIR /srv
CMD sh /srv/entrypoint.sh