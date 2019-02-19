from rest_framework import serializers
from addresses.serializers import AddressSerializer
from .models import MaderaUser


class MaderaUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    address = AddressSerializer(many=True, read_only=True)
    date_joined = serializers.DateTimeField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        model = MaderaUser
        fields = ('id', 'email', 'first_name', 'last_name', 'address', 'date_joined', 'is_active',
                  'is_staff')
        write_only_fields = ('password',)
        read_only_fields = ('address',)

    def create(self, validated_data):
        """
        Create and return a new `MaderaUser` instance, given the validated data.
        """
        return MaderaUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_active)
        instance.save()
        return instance
