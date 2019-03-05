from rest_framework import serializers
from users.serializers import ClientSerializer, SalesPersonSerializer

from users.models import Client, SalesPerson
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField(required=False, default='Brouillon')
    attachment = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    client = ClientSerializer(required=False)
    salesperson = SalesPersonSerializer(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Quote
        fields = ('id', 'price', 'state', 'attachment', 'client', 'salesperson',
                  'created_at', 'updated_at')

    def create(self, validated_data, client=None, salesperson=None):
        for user in ('client', 'salesperson'):
            try:
                user_data = validated_data.pop(user)
            except KeyError as e:
                print(e)
            finally:
                if user == 'client':
                    client = Client.objects.get(user_data)
                    client = Client.objects.create(**user_data)
                    client.save()
                else:
                    user = SalesPerson.objects.create(**user_data)
                    salesperson.save()
                quote = Quote.objects.create(client=client,
                                             salesperson=salesperson,
                                             **validated_data)
        return quote

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)

        if instance.client:
            for k, v in validated_data.get('client').items():
                instance.client.__dict__[k] = v
            instance.client.save(update_fields=validated_data.get('client').keys())
        else:
            address_data = validated_data.get('client')
            instance.client = Client.objects.create(**address_data)
            instance.client.save()

        if instance.salesperson:
            for k, v in validated_data.get('salesperson').items():
                instance.salesperson.__dict__[k] = v
            instance.salesperson.save(update_fields=validated_data.get('salesperson').keys())
        else:
            address_data = validated_data.get('salesperson')
            instance.salesperson = SalesPerson.objects.create(**address_data)
            instance.salesperson.save()
        instance.save()
        return instance
