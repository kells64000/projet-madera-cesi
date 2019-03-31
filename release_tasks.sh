#!/usr/bin/env bash

source bin/activate 

python manage.py migrate
python manage.py loaddata modules components gammes users
