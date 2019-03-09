# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Component, Module, Gamme
from .serializers import ComponentSerializer, ModuleSerializer, GammeSerializer


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


class ListModule(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailModule(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Module.objects.get(pk=pk)
        except Module.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        module = self.get_object(pk)
        serializer = ComponentSerializer(module)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        module = self.get_object(pk)
        serializer = ComponentSerializer(module, data=request.data)
        for field in ['name', 'length', 'width', 'unit']:
            serializer.fields[field].required = False
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        module = self.get_object(pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListGamme(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        gammes = Gamme.objects.all()
        serializer = GammeSerializer(gammes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GammeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailGamme(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Gamme.objects.get(pk=pk)
        except Gamme.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gamme = self.get_object(pk)
        serializer = ComponentSerializer(gamme)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gamme = self.get_object(pk)
        serializer = ComponentSerializer(gamme, data=request.data)
        for field in ['name', 'length', 'width', 'unit']:
            serializer.fields[field].required = False
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gamme = self.get_object(pk)
        gamme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
