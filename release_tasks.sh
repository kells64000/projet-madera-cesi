#!/usr/bin/env bash

docker-compose up -d --build
docker-compose run azure-madera python manage.py migrate --noinput
docker-compose run azure-madera python manage.py loaddata modules components gammes users
