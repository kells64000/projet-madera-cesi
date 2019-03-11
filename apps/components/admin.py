from django.contrib import admin
from .models import Component, Module, Gamme, House


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    fields = ('name', 'component_type', 'nature', 'length', 'width', 'depth', 'unit', 'price',
        'gammes')
    model = Component


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    fields = ('name', 'nature', 'length', 'length2', 'height', 'angle', 'angle_type', 'unit',
        'family', 'designer', 'gammes', 'components')
    model = Module


@admin.register(Gamme)
class GammeAdmin(admin.ModelAdmin):
    fields = ('name', 'ratio')
    model = Gamme


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    fields = ('shape', 'shape_img', 'gammes', 'modules')
    model = House
