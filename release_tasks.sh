##!/bin/bash
#
#docker-compose up -d --build
#docker-compose run azure-madera python manage.py migrate --noinput
#docker-compose run azure-madera python manage.py loaddata modules components gammes users


#!/bin/bash

# Public IP address of your ingress controller
IP="20.188.34.134"

# Name to associate with public IP address
DNSNAME="madera"

# Get the resource-id of the public ip
PUBLICIPID=$(az network public-ip list --query "[?ipAddress!=null]|[?contains(ipAddress, '$IP')].[id]" --output tsv)

# Update public ip address with DNS name
az network public-ip update --ids $PUBLICIPID --dns-name $DNSNAME