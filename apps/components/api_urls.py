# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from . import api_views

urlpatterns = [
    path('components/', api_views.ListComponent.as_view(), name='components'),
    path('components/<int:pk>', api_views.DetailComponent.as_view(), name='component'),
    path('modules/', api_views.ListModule.as_view(), name='modules'),
    url('^modules/family/(?P<family>.+)/$', api_views.ListModuleFamily.as_view(), name='modules-family'),
    path('modules/<int:pk>', api_views.DetailModule.as_view(), name='module'),
    path('gammes/', api_views.ListGamme.as_view(), name='gammes'),
    path('gammes/<int:pk>', api_views.DetailGamme.as_view(), name='gamme'),
    path('houses/', api_views.ListHouse.as_view(), name='houses'),
    url('^houses/shape/(?P<shape>.+)/$', api_views.ListHouseShape.as_view(), name='house-shape'),
    path('houses/<int:pk>', api_views.DetailHouse.as_view(), name='house')
]
