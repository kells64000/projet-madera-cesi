import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django_xhtml2pdf.utils import generate_pdf
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Quote
from .serializers import QuoteListSerializer


@csrf_exempt
def quotes_list(request):
    """
    List all quotes, or create a new quote.
    """
    if request.method == 'GET':
        quotes = Quote.objects.all()
        serializer = QuoteListSerializer(quotes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuoteListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def quotes_detail(request, pk):
    """
    Retrieve update or delete a quote.
    """
    try:
        quote = Quote.objects.get(pk=pk)
    except Quote.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuoteListSerializer(quote)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuoteListSerializer(quote, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        quote.delete()
        return HttpResponse(status=204)


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def quote_2_pdf(request):
    template_path = 'quotes/quote.html'
    context = {
        'quote': 'Mes.super.params.VueJs'
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(Context(context))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response