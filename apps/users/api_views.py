# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MaderaUser, SalesPerson, Client
from .serializers import MaderaUserSerializer, SalesPersonSerializer, ClientSerializer


class ListUser(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        users = MaderaUser.objects.all()
        serializer = MaderaUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        address_data = request.data.get('address', None)
        serializer = MaderaUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(address=address_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUser(APIView):

    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return MaderaUser.objects.get(pk=pk)
        except MaderaUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MaderaUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        address_data = request.data.get('address', None)
        serializer = MaderaUserSerializer(user, data=request.data)
        serializer.fields['email'].required = False
        if serializer.is_valid():
            serializer.save(address=address_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListSalesPerson(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        salespersons = SalesPerson.objects.all()
        serializer = SalesPersonSerializer(salespersons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        address_data = request.data.get('address', None)
        serializer = SalesPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(address=address_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailSalesPerson(APIView):

    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return SalesPerson.objects.get(pk=pk)
        except SalesPerson.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        salesperson = self.get_object(pk)
        serializer = SalesPersonSerializer(salesperson)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address_data = request.data.get('address', None)
        salesperson = self.get_object(pk)
        serializer = SalesPersonSerializer(salesperson, data=request.data)
        for field in ['email', 'workplace']:
            serializer.fields[field].required = False
        if serializer.is_valid():
            serializer.save(address=address_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        salesperson = self.get_object(pk)
        salesperson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListClient(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        address_data = request.data.get('address', None)
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(address=address_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailClient(APIView):

    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address_data = request.data.get('address', None)
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        for field in ['email', 'is_pro']:
            serializer.fields[field].required = False
        if serializer.is_valid():
            serializer.save(address=address_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
