FROM node:10

ADD . /var/www/html/madera
WORKDIR /var/www/html/madera
RUN npm build

FROM python:3.6

WORKDIR /var/www/html/madera
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn madera.wsgi:application --bind 0.0.0.0:8000 --workers 3