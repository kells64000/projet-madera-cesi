# -*- coding: utf-8 -*-
from rest_framework import serializers

from addresses.models import Address
from users.models import MaderaUser
from users.serializers import MaderaUserSerializer
from .models import Component, Module, Gamme


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

    class Meta:
        model = Component
        fields = ('id', 'name', 'nature', 'length', 'width', 'depth', 'unit', 'surface')

    def create(self, validated_data):
        component = Component.objects.create(**validated_data)
        return component

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.depth = validated_data.get('depth', instance.depth)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.price = validated_data.get('price', instance.price)
        instance.family = validated_data.get('family', instance.family)
        instance.save()

        return instance

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by


class ModuleSerializer(serializers.ModelSerializer):

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
    component = ComponentSerializer(required=True, many=True)

    class Meta:
        model = Module
        fields = ('id', 'name', 'nature', 'length', 'width', 'depth', 'unit', 'surface',
                  'component', 'designer', 'designed_by')

    def create(self, validated_data):
        designer = component = None
        try:
            designer_data = validated_data.pop('designer')
            address_data = designer_data.pop('address') if designer_data['address'] else dict()
            if address_data:
                address = Address.objects.create(**address_data)
                address.save()
                designer = MaderaUser.objects.create(address=address, **designer_data)
        except KeyError as e:
            print(e)
        try:
            designer_data = validated_data.pop('component')
            address_data = designer_data.pop('address') if designer_data['address'] else dict()
            if address_data:
                address = Address.objects.create(**address_data)
                address.save()
                component = MaderaUser.objects.create(address=address, **designer_data)
        except KeyError as e:
            print(e)
        module = Module.objects.create(designer=designer, component=component, **validated_data)
        return module

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
        if instance.component:
            for k, v in validated_data.get('component').items():
                instance.component.__dict__[k] = v
            instance.component.save(update_fields=validated_data.get('component').keys())
        else:
            designer_data = validated_data.get('component')
            instance.component = MaderaUser.objects.create(**designer_data)
            instance.component.save()
        instance.save()

        return instance

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by


class GammeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=30)
    nature = serializers.CharField(required=False, max_length=20)
    module = ModuleSerializer(required=False, many=True)

    class Meta:
        model = Module
        fields = ('id', 'name', 'nature')

    def create(self, validated_data):
        gamme = Gamme.objects.create(**validated_data)
        return gamme

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)

        if instance.module:
            for k, v in validated_data.get('module').items():
                instance.module.__dict__[k] = v
            instance.module.save(update_fields=validated_data.get('module').keys())
        else:
            designer_data = validated_data.get('module')
            instance.module = MaderaUser.objects.create(**designer_data)
            instance.module.save()
        instance.save()

        return instance
