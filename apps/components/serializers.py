# -*- coding: utf-8 -*-
from rest_framework import serializers

from users.models import MaderaUser, Provider
from users.serializers import MaderaUserSerializer
from .models import Component, Module, Gamme, House


class ComponentSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, max_length=30)
    # nature = serializers.CharField(required=False, max_length=20)
    # length = serializers.DecimalField(required=True, max_digits=8, decimal_places=2)
    # width = serializers.DecimalField(required=True, max_digits=8, decimal_places=2)
    # depth = serializers.DecimalField(required=False, allow_null=True,
    #                                  max_digits=8, decimal_places=2)
    # unit = serializers.CharField(max_length=10)
    # surface = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Component
        fields = ('__all__')

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
        instance.save()

        return instance

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by

    def to_representation(self, obj):
        ret = super(ComponentSerializer, self).to_representation(obj)
        return ret


class ModuleSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=30)
    nature = serializers.CharField(required=False, max_length=20)
    family = serializers.CharField(required=False, max_length=3)
    length = serializers.DecimalField(required=True, max_digits=8, decimal_places=2)
    width = serializers.DecimalField(required=True, max_digits=8, decimal_places=2)
    depth = serializers.DecimalField(required=False, allow_null=True,
                                     max_digits=8, decimal_places=2)
    unit = serializers.CharField(max_length=10)
    surface = serializers.SerializerMethodField(required=False)
    designer = MaderaUserSerializer(required=False)
    designed_by = serializers.SerializerMethodField()
    components = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ('__all__')

    def create(self, validated_data):
        designer = component = None
        designer_data = validated_data.pop('designer', None)
        component_data = validated_data.pop('components', None)
        if designer_data:
            designer = Provider.objects.get_or_create(**designer_data)[0]
        module = Module.objects.create(designer=designer, **validated_data)
        if component_data:
            components_list = list()
            for comp_id in component_data:
                component = Component.objects.get_or_create(id=comp_id)[0]
                components_list.append(component)
        module.components.set(components_list)
        module.save()
        return module

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.depth = validated_data.get('depth', instance.depth)
        instance.family = validated_data.get('family', instance.family)

        if instance.designer:
            for k, v in validated_data.get('designer').items():
                instance.designer.__dict__[k] = v
            instance.designer.save(update_fields=validated_data.get('designer').keys())
        else:
            designer_data = validated_data.get('designer')
            if designer_data:
                instance.designer = MaderaUser.objects.create(**designer_data)
                instance.designer.save()
        if instance.component:
            for k, v in validated_data.get('components').items():
                instance.component.__dict__[k] = v
            instance.component.save(update_fields=validated_data.get('components').keys())
        else:
            component_data = validated_data.get('components')
            if component_data:
                instance.component = MaderaUser.objects.create(**component_data)
                instance.component.save()
        instance.save()

        return instance

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by

    def get_components(self, obj):
        serializer = ComponentSerializer(obj.get_components(), many=True, context=self.context)
        return serializer.data

    def to_representation(self, obj):
        ret = super(ModuleSerializer, self).to_representation(obj)
        return ret


class GammeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=30)
    nature = serializers.CharField(required=False, max_length=20)
    modules = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ('id', 'name', 'nature', 'modules')

    def create(self, validated_data):
        module_data = validated_data.pop('modules', None)
        gamme = Gamme.objects.create(**validated_data)
        if module_data:
            for module in module_data:
                for module_dict in module:
                    module = Module.objects.get_or_create(**module_dict)[0]
                    gamme.module_set.add(module)
        return gamme

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)

        if instance.module:
            for k, v in validated_data.get('modules').items():
                instance.module.__dict__[k] = v
            instance.module.save(update_fields=validated_data.get('modules').keys())
        else:
            designer_data = validated_data.get('modules', None)
            if designer_data:
                instance.module = MaderaUser.objects.create(**designer_data)
                instance.module.save()
        instance.save()

        return instance

    def get_modules(self, obj):
        serializer = ModuleSerializer(obj.get_modules(), many=True, context=self.context)
        return serializer.data


class HouseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    shape = serializers.CharField(required=False, max_length=20)
    modules = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = House
        fields = ('id', 'shape', 'modules')

    def create(self, validated_data):
        module_data = validated_data.pop('modules', None)
        house = House.objects.create(**validated_data)
        if module_data:
            for module in module_data:
                for module_dict in module:
                    module = Module.objects.get_or_create(**module_dict)[0]
                    house.module_set.add(module)
        return house

    def update(self, instance, validated_data):
        instance.shape = validated_data.get('shape', instance.shape)

        if instance.modules:
            for k, v in validated_data.get('modules').items():
                instance.modules.__dict__[k] = v
            instance.module.save(update_fields=validated_data.get('modules').keys())
        else:
            module_dict = validated_data.get('modules', None)
            if module_dict:
                instance.modules = Module.objects.create(**module_dict)
                instance.modules.save()
        instance.save()
        return instance

    def get_modules(self, obj):
        serializer = ModuleSerializer(obj.get_modules(), many=True, context=self.context)
        return serializer.data
