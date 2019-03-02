# -*- coding: utf-8 -*-
from rest_framework import serializers
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
    surface = serializers.SerializerMethodField()
    designer = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ('id', 'name', 'nature', 'length', 'width', 'depth', 'unit', 'surface',
                  'designer')

    def get_surface(self, obj):
        return obj.surface

    def get_designer(self, obj):
        return obj.designed_by
