#FROM node:10
#
#WORKDIR /var/www/html/madera
#RUN npm run prod

FROM python:3.6

ADD . /var/www/html/madera

WORKDIR /var/www/html/madera
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt