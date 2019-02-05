from rest_framework import serializers
from .models import MaderaUser


class MaderaUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    location = serializers.CharField(required=False, allow_blank=True, max_length=30)
    date_joined = serializers.DateTimeField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField(default=False)

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
        instance.location = validated_data.get('location', instance.location)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_active)
        instance.save()
        return instance
