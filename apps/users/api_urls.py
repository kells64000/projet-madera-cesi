from django.urls import path
from . import api_views

urlpatterns = [
    path('users/', api_views.ListUser.as_view(), name='users'),
    path('users/<uuid:pk>', api_views.DetailUser.as_view(), name='user'),
    path('salespersons/', api_views.ListSalesPerson.as_view(), name='salespersons'),
    path('salespersons/<uuid:pk>', api_views.DetailSalesPerson.as_view(), name='salesperson'),
    path('clients/', api_views.ListClient.as_view(), name='clients'),
    path('clients/<uuid:pk>', api_views.DetailClient.as_view(), name='client'),

]
