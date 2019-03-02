# -*- coding: utf-8 -*-
from django.urls import path
from . import api_views

urlpatterns = [
    path('components/', api_views.ListComponent.as_view(), name='components'),
    path('components/<int:pk>', api_views.DetailComponent.as_view(), name='component')
]
