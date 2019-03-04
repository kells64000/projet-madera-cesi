# -*- coding: utf-8 -*-
from rest_framework import serializers

from addresses.models import Address
from users.models import MaderaUser
from users.serializers import MaderaUserSerializer
from .models import Component


class ComponentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=30)
    nature = serializers.CharField(required=False, max_length=20)
    length = serializers.DecimalField(required=True, max_digits=8, decimal_places=2)
    width = serializers.DecimalField(required=True, max_digits=8, decimal_places=2)
    depth = serializers.DecimalField(required=False, allow_null=True,
                                     max_digits=8, decimal_places=2)
    unit = serializers.CharField(max_length=10)
    surface = serializers.SerializerMethodField(required=False)
    designer = MaderaUserSerializer(required=False)
    designed_by = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ('id', 'name', 'nature', 'length', 'width', 'depth', 'unit', 'surface',
                  'designer', 'designed_by')

    def create(self, validated_data):
        designer = None
        try:
            designer_data = validated_data.pop('designer')
            address_data = designer_data.pop('address') if designer_data['address'] else dict()
            if address_data:
                address = Address.objects.create(**address_data)
                address.save()
                designer = MaderaUser.objects.create(address=address, **designer_data)
        except KeyError as e:
            print(e)
        component = Component.objects.create(designer=designer, **validated_data)
        return component

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.depth = validated_data.get('depth', instance.depth)

        if instance.designer:
            for k, v in validated_data.get('designer').items():
                instance.designer.__dict__[k] = v
            instance.designer.save(update_fields=validated_data.get('designer').keys())
        else:
            designer_data = validated_data.get('designer')
            instance.designer = MaderaUser.objects.create(**designer_data)
            instance.designer.save()
        instance.save()

        return instance

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by
