from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Quote
from .renderers import QuoteJSONRenderer
from .serializers import QuoteListSerializer


class QuoteListApiView(ListAPIView):
    model = Quote
    queryset = Quote.objects.all()
    # authentication_class = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    renderer_classes = (QuoteJSONRenderer, )
    serializer_class = QuoteListSerializer


class QuoteRetrieveApiView(RetrieveAPIView):
    # authentication_class = (JSONWebTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    renderer_classes = (QuoteJSONRenderer, )
    serializer_class = QuoteListSerializer

    def retrieve(self, request, quote, *args, **kwargs):
        quote = Quote.objects.get(id=quote.id)
        serializer = self.serializer_class(quote)

        return Response(serializer.data, status=status.HTTP_200_OK)
