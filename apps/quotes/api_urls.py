from django.urls import path
from . import api_views

urlpatterns = [
    path('quotes/', api_views.ListQuote.as_view(), name='quotes'),
    path('quotes/<int:pk>', api_views.DetailQuote.as_view(), name='quote'),
    path('quotes/<int:pk>/pdf', api_views.DetailQuote.as_view(), name='quote2pdf')
]
