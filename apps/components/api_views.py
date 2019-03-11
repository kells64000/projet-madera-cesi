# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Component, Module, Gamme, House
from .serializers import ComponentSerializer, ModuleSerializer, GammeSerializer, HouseSerializer


class ListComponent(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        gammes_data = request.data.get('gammes', None)
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(gammes=gammes_data)
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
        gammes_data = request.data.get('gammes', None)
        serializer = ComponentSerializer(component, data=request.data)
        if serializer.is_valid():
            serializer.save(gammes=gammes_data)
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
        component_data = request.data.get('components', None)
        gammes_data = request.data.get('gammes', None)
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(components=component_data, gammes=gammes_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListModuleFamily(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ModuleSerializer

    def get_queryset(self):
        queryset = Module.objects.all()
        family = self.kwargs['family'].upper()
        if family:
            queryset = queryset.filter(family=family)
        return queryset


class DetailModule(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Module.objects.get(pk=pk)
        except Module.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        module = self.get_object(pk)
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        module = self.get_object(pk)
        component_data = request.data.get('components', None)
        gammes_data = request.data.get('gammes', None)
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save(components=component_data, gammes=gammes_data)
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
        serializer = GammeSerializer(gamme)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gamme = self.get_object(pk)
        serializer = GammeSerializer(gamme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gamme = self.get_object(pk)
        gamme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListHouse(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        module_data = request.data.get('modules', None)
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(modules=module_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListHouseShape(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HouseSerializer

    def get_queryset(self):
        queryset = House.objects.all()
        shape = self.kwargs['shape']
        if shape:
            queryset = queryset.filter(shape=shape)
        return queryset


class DetailHouse(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        house = self.get_object(pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        house = self.get_object(pk)
        module_data = request.data.get('modules', None)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save(modules=module_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        house = self.get_object(pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
