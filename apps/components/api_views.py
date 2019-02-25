# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Component
from .serializers import ComponentSerializer


@csrf_exempt
def components_list(request):
    """
    List all components, or create a new component.
    """
    if request.method == 'GET':
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComponentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def components_detail(request, pk):
    """
    Retrieve update or delete a component.
    """
    try:
        component = Component.objects.get(pk=pk)
    except Component.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ComponentSerializer(component)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ComponentSerializer(component, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        component.delete()
        return HttpResponse(status=204)
