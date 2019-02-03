from django.urls import path
from . import views, api_views

urlpatterns = [
    path('user/', api_views.user_list),
    path('user/<int:pk>', api_views.user_detail)
]
