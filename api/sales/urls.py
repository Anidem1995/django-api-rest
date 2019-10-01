from django.urls import path
from .views import ListClientsView


urlpatterns = [
    path('clients/', ListClientsView.as_view(), name="clients-all")
]