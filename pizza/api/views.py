from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PizzaVaultCreate(generics.CreateAPIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = PizzaVault.objects.all()
	serializer_class = PizzaVaultSerializer

class PizzaVaultList(generics.ListAPIView):
	queryset = PizzaVault.objects.all()
	serializer_class = PizzaVaultSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['types', 'size']

class PizzaVaultDetail(generics.RetrieveUpdateDestroyAPIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = PizzaVault.objects.all()
	serializer_class = PizzaVaultSerializer