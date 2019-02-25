# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import MaderaUser
from .serializers import MaderaUserSerializer


@csrf_exempt
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        maderausers = MaderaUser.objects.all()
        serializer = MaderaUserSerializer(maderausers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaderaUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        maderauser = MaderaUser.objects.get(pk=pk)
    except MaderaUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MaderaUserSerializer(maderauser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MaderaUserSerializer(maderauser, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        maderauser.delete()
        return HttpResponse(status=204)
