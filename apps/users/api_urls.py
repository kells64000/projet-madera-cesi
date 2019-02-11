from django.urls import path
from . import api_views

urlpatterns = [
    path('users/', api_views.user_list),
    path('user/<int:pk>', api_views.user_detail)
]
