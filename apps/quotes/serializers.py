from rest_framework import serializers
from users.serializers import ClientSerializer, SalesPersonSerializer

from users.models import Client, SalesPerson
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=20)
    reference = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField(required=False, default='Brouillon')
    attachment = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Quote
        fields = ('id', 'name', 'reference', 'price', 'state', 'attachment',
                  'client', 'salesperson', 'created_at', 'updated_at')

    def create(self, validated_data):
        client_data = validated_data.pop('client', None)
        salesperson_data = validated_data.pop('salesperson', None)
        quote = Quote.objects.create(**validated_data)
        if client_data:
            client = Client.objects.get_or_create(id=client_data.get('id'))[0]
            client.save()
            quote.client_id = client.id
        if salesperson_data:
            salesperson = SalesPerson.objects.get_or_create(id=salesperson_data.get('id'))[0]
            salesperson.save()
            quote.salesperson_id = salesperson.id
        quote.save()
        return quote

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.reference = validated_data.get('reference', instance.reference)
        instance.price = validated_data.get('price', instance.price)
        instance.state = validated_data.get('state', instance.state)
        instance.attachment = validated_data.get('attachment', instance.attachment)
        client_data = validated_data.pop('client', None)
        salesperson_data = validated_data.pop('salesperson', None)

        if client_data:
            client, created = Client.objects.update_or_create(id=client_data.get('id'))
            if created:
                client.save()
            instance.client_id = client.id
        if salesperson_data:
            salesperson, created = SalesPerson.objects.update_or_create(id=salesperson_data.get('id'))
            if created:
                salesperson.save()
            instance.salesperson_id = salesperson.id
        instance.save()
        return instance
