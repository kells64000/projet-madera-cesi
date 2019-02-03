from django.conf.urls import url
from .views import QuoteListApiView, QuoteRetrieveApiView

app_name = 'quotes'
urlpatterns = [
    url(r'^quotes/$', QuoteListApiView.as_view()),
    url(r'^quotes/(?P<quote_id>\w+)/?$', QuoteRetrieveApiView.as_view()),
]