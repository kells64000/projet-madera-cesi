#!/usr/bin/env bash

docker-compose up -d --build
docker-compose run web python manage.py migrate --noinput
docker-compose run web python manage.py loaddata modules components gammes users
