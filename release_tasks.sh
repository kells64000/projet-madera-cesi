#!/usr/bin/env bash

python manage.py migrate
python manage.py loaddata modules components gammes users
