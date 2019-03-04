# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Component
from .serializers import ComponentSerializer


class ListComponent(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailComponent(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Component.objects.get(pk=pk)
        except Component.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        component = self.get_object(pk)
        serializer = ComponentSerializer(component)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        component = self.get_object(pk)
        serializer = ComponentSerializer(component, data=request.data)
        for field in ['name', 'length', 'width', 'unit']:
            serializer.fields[field].required = False
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        component = self.get_object(pk)
        component.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
