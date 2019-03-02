from django.urls import path
from . import api_views

urlpatterns = [
    path('addresses/', api_views.ListAddress.as_view(), name='addresses'),
    path('addresses/<int:pk>', api_views.DetailAddress.as_view(), name='address')
]
