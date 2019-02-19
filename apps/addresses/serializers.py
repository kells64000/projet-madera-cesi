from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(required=True)
    zipcode = serializers.CharField(required=False, allow_blank=True, max_length=8)
    city = serializers.CharField(required=False, allow_blank=True, max_length=50)
    country = serializers.CharField(required=False, allow_blank=True, max_length=30)

    class Meta:
        model = Address
        fields = ('street', 'zipcode', 'city', 'country')
        exclude = ('latitude', 'longitude')

    def create(self, validated_data):
        """
        Create and return a new `MaderaUser` instance, given the validated data.
        """
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.street = validated_data.get('email', instance.email)
        instance.zipcode = validated_data.get('first_name', instance.first_name)
        instance.city = validated_data.get('last_name', instance.last_name)
        instance.country = validated_data.get('address', instance.address)

        instance.save()
        return instance
