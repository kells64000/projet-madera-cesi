# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import Http404, JsonResponse, HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from xhtml2pdf import pisa

from .models import Quote
from .serializers import QuoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class ListQuote(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        client_data = request.data.pop('client', None)
        salesperson_data = request.data.pop('salesperson', None)
        house_data = request.data.pop('house', None)
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=client_data, salesperson=salesperson_data, house=house_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailQuote(APIView):

    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        quote = self.get_object(pk)
        client_data = request.data.pop('client', None)
        salesperson_data = request.data.pop('salesperson', None)
        house_data = request.data.pop('house', None)

        serializer = QuoteSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save(client=client_data, salesperson=salesperson_data, house=house_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        quote = self.get_object(pk)
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def generate_pdf(request):
    template_path = 'quotes/quote.html'
    context = json.loads(request.body.decode('utf-8'))

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Devis-{ref}.pdf"'.format(
        ref=context['ref'])

    html = render_to_string(template_path, context)
    filename = 'quote_{}.pdf'.format(context.get('ref'))
    pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    with open('assets/pdf/' + filename, 'wb') as f:
        f.write(response.content)

    # Envoi email
    subject, from_email, to = 'Madera', 'no-reply@madera.com', context.get('client').get('email')
    text_content = 'Bonjour ' + context.get("client").get("full_name") + ',<p>Veuillez trouver ci-joint le devis.</p><p>Ceci est un email automatique merci de ne pas y repondre.</p><p>Entreprise Madera</p>'
    msg = EmailMessage(subject, text_content, from_email, [to])
    msg.attach_file('assets/pdf/' + filename)
    msg.send()

    return JsonResponse({"filename": filename})


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/

    # convert URIs to absolute system paths
    if uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl)
            )
    return path
