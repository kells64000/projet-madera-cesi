from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(required=False, allow_blank=True, max_length=80)
    zipcode = serializers.CharField(required=False, allow_blank=True, max_length=30)
    city = serializers.CharField(required=False, allow_blank=True, max_length=30)
    country = serializers.CharField(required=False, allow_blank=True, max_length=12)

    class Meta:
        model = Address
        fields = ('__all__')

    def create(self, validated_data, address=None):
        address = Address.objects.create(**validated_data)
        return address

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
