# -*- coding: utf-8 -*-
from django.urls import path
from . import api_views

urlpatterns = [
    path('components/', api_views.components_list),
    path('components/<int:pk>', api_views.components_detail)
]
