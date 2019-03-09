# -*- coding: utf-8 -*-
from django.urls import path
from . import api_views

urlpatterns = [
    path('components/', api_views.ListComponent.as_view(), name='components'),
    path('components/<int:pk>', api_views.DetailComponent.as_view(), name='component'),
    path('modules/', api_views.ListModule.as_view(), name='modules'),
    path('modules/<int:pk>', api_views.DetailModule.as_view(), name='module'),
    path('gammes/', api_views.ListGamme.as_view(), name='gammes'),
    path('gamme/<int:pk>', api_views.DetailGamme.as_view(), name='gamme')
]
