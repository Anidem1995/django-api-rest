from rest_framework import serializers
from .models import Client

class ClientDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("name", "address", "email", "phone")

