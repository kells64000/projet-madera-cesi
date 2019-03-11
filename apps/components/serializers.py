# -*- coding: utf-8 -*-
from rest_framework import serializers

from users.models import MaderaUser, Provider
from users.serializers import MaderaUserSerializer
from .constants import FAMILY_CHOICES, NATURE_CHOICES, GAMME_CHOICES, SHAPE_CHOICES
from .models import Component, Module, Gamme, House


class GammeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.ChoiceField(choices=GAMME_CHOICES, required=False, allow_blank=True)
    ratio = serializers.DecimalField(required=False, max_digits=4, decimal_places=2)

    class Meta:
        model = Module
        fields = ('id', 'name', 'ratio')

    def create(self, validated_data):
        gamme = Gamme.objects.create(**validated_data)
        return gamme

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ratio = validated_data.get('ratio', instance.ratio)
        instance.save()

        return instance

    def to_representation(self, obj):
        ret = super(GammeSerializer, self).to_representation(obj)
        return ret


class ComponentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=30)
    component_type = serializers.CharField(required=False, max_length=30, allow_blank=True)
    nature = serializers.ChoiceField(choices=NATURE_CHOICES, required=False, allow_blank=True)
    length = serializers.DecimalField(required=False, max_digits=8, decimal_places=2,
        allow_blank=True)
    width = serializers.DecimalField(required=False, max_digits=8, decimal_places=2,
        allow_blank=True)
    unit = serializers.CharField(required=False, max_length=10)
    surface = serializers.SerializerMethodField(required=False)
    price = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)
    total_price = serializers.SerializerMethodField(required=False)
    quantity = serializers.IntegerField(required=False)
    gammes = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ('__all__')

    def create(self, validated_data):
        gamme_data = validated_data.pop('gammes', None)
        component = Component.objects.create(**validated_data)
        if gamme_data:
            gammes_list = list()
            for gamme_id in gamme_data:
                gamme = Gamme.objects.get_or_create(id=gamme_id)[0]
                gammes_list.append(gamme)
            component.gammes.set(gammes_list)
        component.save()
        return component

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.component_type = validated_data.get('component_type', instance.component_type)
        instance.nature = validated_data.get('nature', instance.nature)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        gammes_data = validated_data.get('gammes')
        gammes_list = list()
        if gammes_data:
            for gamme_id in gammes_data:
                gamme = Gamme.objects.get_or_create(id=gamme_id)[0]
                gammes_list.append(gamme)
            instance.gammes.set(gammes_list)
        instance.save()

        return instance

    def get_total_price(self, obj):
        return obj.total_price

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by

    def get_gammes(self, obj):
        serializer = GammeSerializer(obj.get_gammes(), many=True, context=self.context)
        return serializer.data

    def to_representation(self, obj):
        ret = super(ComponentSerializer, self).to_representation(obj)
        return ret


class ModuleSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=30)
    nature = serializers.CharField(required=False, max_length=20)
    family = serializers.CharField(required=False, max_length=3)
    length = serializers.DecimalField(required=False, max_digits=8, decimal_places=2,
        allow_blank=True)
    length2 = serializers.DecimalField(required=False, max_digits=8, decimal_places=2,
        allow_blank=True)
    height = serializers.DecimalField(required=False, max_digits=8, decimal_places=2,
        allow_blank=True)
    unit = serializers.CharField(required=False, max_length=10, allow_blank=True)
    surface = serializers.SerializerMethodField(required=False)
    family = serializers.ChoiceField(choices=FAMILY_CHOICES, required=False, allow_blank=True)
    designer = MaderaUserSerializer(required=False)
    designed_by = serializers.SerializerMethodField()
    components = serializers.SerializerMethodField()
    gammes = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ('__all__')

    def create(self, validated_data):
        designer = component = None
        designer_data = validated_data.pop('designer', None)
        component_data = validated_data.pop('components', None)
        gamme_data = validated_data.get('gammes', None)
        if designer_data:
            designer = Provider.objects.get_or_create(**designer_data)[0]
        module = Module.objects.create(designer=designer, **validated_data)
        if component_data:
            components_list = list()
            for comp_id in component_data:
                component = Component.objects.get_or_create(id=comp_id)[0]
                components_list.append(component)
            module.components.set(components_list)
        if gamme_data:
            gammes_list = list()
            for gamme_id in gamme_data:
                gamme = Gamme.objects.get_or_create(id=gamme_id)[0]
                gammes_list.append(gamme)
            module.gammes.set(gammes_list)
        module.save()
        return module

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)
        instance.length = validated_data.get('length', instance.length)
        instance.height = validated_data.get('height', instance.height)
        instance.family = validated_data.get('family', instance.family)
        components_data = validated_data.get('components')
        gammes_data = validated_data.get('gammes')

        if instance.designer:
            for k, v in validated_data.get('designer').items():
                instance.designer.__dict__[k] = v
            instance.designer.save(update_fields=validated_data.get('designer').keys())
        else:
            designer_data = validated_data.get('designer')
            if designer_data:
                instance.designer = MaderaUser.objects.create(**designer_data)
                instance.designer.save()
        components_list = list()
        if components_data:
            for component_id in components_data:
                component = Component.objects.get_or_create(id=component_id)[0]
                components_list.append(component)
            instance.components.set(components_list)
        gammes_list = list()
        if gammes_data:
            for gamme_id in gammes_data:
                gamme = Gamme.objects.get_or_create(id=gamme_id)[0]
                gammes_list.append(gamme)
            instance.components.set(gammes_list)
        instance.save()

        return instance
        instance.save()

        return instance

    def get_surface(self, obj):
        return obj.surface

    def get_designed_by(self, obj):
        return obj.designed_by

    def get_components(self, obj):
        serializer = ComponentSerializer(obj.get_components(), many=True, context=self.context)
        return serializer.data

    def get_gammes(self, obj):
        serializer = GammeSerializer(obj.get_gammes(), many=True, context=self.context)
        return serializer.data

    def to_representation(self, obj):
        ret = super(ModuleSerializer, self).to_representation(obj)
        return ret

    def get_price(self, obj):
        return obj.calculated_price


class HouseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    shape = serializers.ChoiceField(choices=SHAPE_CHOICES, required=False, allow_blank=True)
    modules = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = ('id', 'shape', 'modules', 'price')

    def create(self, validated_data):
        module_data = validated_data.pop('modules', None)
        house = House.objects.create(**validated_data)
        if module_data:
            modules_list = list()
            for module_id in module_data:
                module = Module.objects.get_or_create(id=module_id)[0]
                modules_list.append(module)
        house.modules.set(modules_list)
        house.save()
        return house

    def update(self, instance, validated_data):
        instance.shape = validated_data.get('shape', instance.shape)
        modules_data = validated_data.get('modules')

        modules_list = list()
        if modules_data:
            for module_id in modules_data:
                module = Module.objects.get_or_create(id=module_id)[0]
                modules_list.append(module)
            instance.modules.set(modules_list)
        instance.save()

        return instance

    def get_modules(self, obj):
        serializer = ModuleSerializer(obj.get_modules(), many=True, context=self.context)
        return serializer.data

    def get_price(self, obj):
        return obj.total_price
