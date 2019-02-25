# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Component


class ComponentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    nature = serializers.CharField(max_length=20)
    length = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    width = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    depth = serializers.DecimalField(allow_null=True, max_digits=10, decimal_places=2)
    unit = serializers.CharField(max_length=10)

    class Meta:
        model = Component
        fields = ('id', 'name', 'nature', 'length', 'width', 'depth', 'unit')

    def create(self, validated_data):
        """
        Create and return a new `Component` instance, given the validated data.
        """
        return Component.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.nature = validated_data.get('nature', instance.nature)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.depth = validated_data.get('depth', instance.depth)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.save()
        return instance
