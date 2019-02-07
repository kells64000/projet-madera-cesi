from django.urls import path
from . import api_views

urlpatterns = [
    path('quotes/', api_views.quotes_list),
    path('quotes/<int:pk>', api_views.quotes_detail)
]
