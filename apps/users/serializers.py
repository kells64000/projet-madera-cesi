# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from rest_exceptions import CustomValidation
from rest_framework import serializers, status

from addresses.models import Address
from addresses.serializers import AddressSerializer
from .models import MaderaUser, SalesPerson, Client, Provider


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MaderaUserSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    full_name = serializers.SerializerMethodField()
    phone = serializers.CharField(required=False, allow_blank=True, max_length=12)
    address = AddressSerializer(required=False)

    date_joined = serializers.DateTimeField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        model = MaderaUser
        fields = ('id', 'email', 'first_name', 'last_name', 'full_name', 'phone',
                  'address', 'date_joined', 'is_active', 'is_staff')
        write_only_fields = ('password',)
        depth = 1

    def validate_email(self, value):
        if MaderaUser.objects.filter(email=value).exists():
            raise CustomValidation("Duplication d'email",
                'email',
                status_code=status.HTTP_409_CONFLICT)
        return value

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        user = MaderaUser.objects.create(**validated_data)
        if address_data:
            if address_data.get('id'):
                address = Address.objects.get(id=address_data.get('id'))[0]
                if address:
                    user.address = address
                    user.save()
            else:
                address = Address.objects.create(**address_data)
                user.address = address
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        address_data = validated_data.get('address', None)
        if address_data:
            if instance.address:
                if address_data.get('id'):
                    address = Address.objects.get(id=address_data.get('id'))[0]
                    if address:
                        instance.address = address
                        instance.save()
                else:
                    address = Address.objects.create(**address_data)
                    instance.address = address
        instance.save()
        return instance

    def to_representation(self, obj):
        """Exclude password from returning dict"""
        ret = super(MaderaUserSerializer, self).to_representation(obj)
        ret.pop('password', None)
        return ret

    def get_full_name(self, obj):
        return obj.get_full_name


class SalesPersonSerializer(MaderaUserSerializer):

    workplace = serializers.CharField(required=True, allow_blank=False, max_length=50)

    class Meta(MaderaUserSerializer.Meta):
        model = SalesPerson
        fields = MaderaUserSerializer.Meta.fields + ('workplace',)

    def create(self, validated_data, address=None):
        address_data = validated_data.pop('address', None)
        salesperson = SalesPerson.objects.create(**validated_data)
        if address_data:
            if address_data.get('id'):
                address = Address.objects.get(id=address_data.get('id'))[0]
                if address:
                    salesperson.address = address
                    salesperson.save()
            else:
                address = Address.objects.create(**address_data)
                salesperson.address = address
        return salesperson

    def update(self, instance, validated_data, address=None):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        address_data = validated_data.get('address', None)
        if address_data:
            if instance.address:
                if address_data.get('id'):
                    address = Address.objects.get(id=address_data.get('id'))[0]
                    if address:
                        instance.address = address
                        instance.save()
                else:
                    address = Address.objects.create(**address_data)
                    instance.address = address
        instance.save()
        return instance


class ClientSerializer(MaderaUserSerializer):

    is_pro = serializers.BooleanField()
    company = serializers.CharField(required=False, allow_blank=True, max_length=50)

    class Meta(MaderaUserSerializer.Meta):
        model = Client
        fields = MaderaUserSerializer.Meta.fields + ('is_pro', 'company')

    def create(self, validated_data, address=None):
        address_data = validated_data.pop('address', None)
        client = Client.objects.create(**validated_data)
        if address_data:
            if address_data.get('id'):
                address = Address.objects.get(id=address_data.get('id'))[0]
                if address:
                    client.address = address
                    client.save()
            else:
                address = Address.objects.create(**address_data)
                client.address = address
        return client

    def update(self, instance, validated_data, address=None):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        address_data = validated_data.get('address', None)
        if address_data:
            if instance.address:
                if address_data.get('id'):
                    address = Address.objects.get(id=address_data.get('id'))[0]
                    if address:
                        instance.address = address
                        instance.save()
                else:
                    address = Address.objects.create(**address_data)
                    instance.address = address
        instance.save()
        return instance


class ProviderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    full_name = serializers.SerializerMethodField()
    phone = serializers.CharField(required=False, allow_blank=True, max_length=12)
    address = AddressSerializer(required=False)

    def create(self, validated_data, address=None):
        address_data = validated_data.pop('address', None)
        provider = Provider.objects.create(**validated_data)
        if address_data:
            if address_data.get('id'):
                address = Address.objects.get(id=address_data.get('id'))[0]
                if address:
                    provider.address = address
                    provider.save()
            else:
                address = Address.objects.create(**address_data)
                provider.address = address
        return provider

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        address_data = validated_data.get('address', None)

        if address_data:
            if instance.address:
                if address_data.get('id'):
                    address = Address.objects.get(id=address_data.get('id'))[0]
                    if address:
                        instance.address = address
                        instance.save()
                else:
                    address = Address.objects.create(**address_data)
                    instance.address = address
        instance.save()
        return instance

    def get_full_name(self, obj):
        return obj.get_full_name
