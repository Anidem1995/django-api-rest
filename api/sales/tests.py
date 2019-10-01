from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Client
from .serializers import ClientDeserializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_client(name="", address="", email="", phone=""):
        if name != "" and address != "" and email != "" and phone != "":
            Client.objects.Create(name=name, address=address, email=email, phone=phone)

    def setUp(self):
        self.create_client("Laura Gallardo", "Matamoros #27", "laura@laura", "1234567890")
        self.create_client("José Medina", "San Carlos #16B", "jose@jose", "9876543210")

    def GetAllClientsTest(BaseViewTest):

        def test_get_all_clients(self):
            response = self.client.get(
                reverse("clients-all", kwargs={"version": "v1"})
            )
            expected = Client.objects.all()
            serialized = ClientDeserializer(expected, many=True)
            self.assertEqual(response.data, serialized.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)