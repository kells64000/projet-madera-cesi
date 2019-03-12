# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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

def generate_pdf(request):

    template_path = 'quotes/quote.html'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Devis-{ref}.pdf"'.format(
        ref=request.ref)

    context = {
        'project': request.name,
        'ref': request.ref,
        'client': request.client,
        'salesperson': request.salesperson,
        'modules': request.modules,
        'TVA': 0.2,
        'price': request.price,
        'today': request.date
    }
    html = render_to_string(template_path, context)

    pisaStatus = pisa.CreatePDF(html, dest=response)

    # Envoi email
    subject, from_email, to = 'Madera', 'no-reply@madera.com', request.client.email
    text_content = 'Veuillez trouver ci-joint le devis'
    msg = EmailMessage(subject, text_content, from_email, [to])
    msg.attach_file(response)
    msg.send()

    return response


# def generate_pdf(request, pk):
#     quote = Quote.objects.get(pk=pk)
#     template_path = 'quotes/quote.html'
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="Devis-{ref}.pdf"'.format(
#         ref=quote.reference)
#
#     context = {
#         'quote': quote,
#         'client': quote.client,
#         'house': quote.house,
#         'VAT': 0.2,
#         'today': datetime.today()
#     }
#     html = render_to_string(template_path, context)
#
#     pisaStatus = pisa.CreatePDF(html, dest=response)
#
#     # Envoi email
#     # subject, from_email, to = 'Madera', 'no-reply@madera.com', ''
#     # text_content = 'Veuillez trouver ci-joint le devis'
#     # msg = EmailMessage(subject, text_content, from_email, [to])
#     # msg.attach_file('')
#     # msg.send()
#
#     return response

# def generate_pdf(request, pk):
#     import ipdb; ipdb.set_trace()
#     quote = Quote.objects.get(pk=pk)
#     template_path = 'quotes/quote.html'
#     context = {
#         'quote': quote
#     }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context=context)

#     # create a pdf
#     pisaStatus = pisa.CreatePDF(
#        html, dest=response, link_callback=quote.link_callback())
#     # if error then show some funy view
#     if pisaStatus.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')

#     # Envoi email
#     subject, from_email, to = 'Madera', 'no-reply@madera.com', quote.client__email
#     text_content = 'Veuillez trouver ci-joint le devis'
#     msg = EmailMessage(subject, text_content, from_email, [to])
#     msg.attach_file('/assets/pdf/client1-facture_exemple.pdf')
#     msg.send()

#     return response


# def link_callback(self, uri, rel):
#     """
#     Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#     resources
#     """
#     # use short variable names
#     sUrl = settings.STATIC_URL      # Typically /static/
#     sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
#     mUrl = settings.MEDIA_URL       # Typically /static/media/
#     mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

#     # convert URIs to absolute system paths
#     if uri.startswith(mUrl):
#         path = os.path.join(mRoot, uri.replace(mUrl, ""))
#     elif uri.startswith(sUrl):
#         path = os.path.join(sRoot, uri.replace(sUrl, ""))
#     else:
#         return uri  # handle absolute uri (ie: http://some.tld/foo.png)

#     # make sure that file exists
#     if not os.path.isfile(path):
#             raise Exception(
#                 'media URI must start with %s or %s' % (sUrl, mUrl)
#             )
#     return path
