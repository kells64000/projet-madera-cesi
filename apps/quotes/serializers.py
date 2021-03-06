from rest_framework import serializers
from .models import Quote
from components.models import House
from users.models import Client, SalesPerson


class QuoteSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=255)
    reference = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField(required=False, default='Brouillon')
    attachment = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Quote
        fields = ('id', 'name', 'reference', 'price', 'state', 'attachment',
                  'client', 'salesperson', 'house', 'created_at', 'updated_at')

    def create(self, validated_data):
        client_data = validated_data.pop('client', None)
        salesperson_data = validated_data.pop('salesperson', None)
        house_data = validated_data.pop('house', None)
        quote = Quote.objects.create(**validated_data)
        if client_data:
            client = Client.objects.get_or_create(id=client_data.get('id'))[0]
            client.save()
            quote.client_id = client.id
        if salesperson_data:
            salesperson = SalesPerson.objects.get_or_create(id=salesperson_data.get('id'))[0]
            salesperson.save()
            quote.salesperson_id = salesperson.id
        if house_data:
            house = House.objects.get_or_create(id=house_data.get('id'))[0]
            house.save()
            quote.salesperson_id = house.id
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
        house_data = validated_data.pop('house', None)

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
        if salesperson_data:
            house, created = House.objects.update_or_create(id=house_data.get('id'))
            if created:
                house.save()
            instance.salesperson_id = house.id
        instance.save()
        return instance
