from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializers import ClientDeserializer


# Create your views here.
class ListClientsView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDeserializer
