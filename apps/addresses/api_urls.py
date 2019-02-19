from django.urls import path
from . import api_views

urlpatterns = [
    path('addresses/', api_views.addresses_list),
    path('addresses/<int:pk>', api_views.addresses_detail)
]
