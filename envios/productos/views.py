from django.shortcuts import render
from rest_framework import generics
from .models import Mascarilla, Pedido
from .serializers import MascarillaSerializer, PedidoSerializer

# Create your views here.

class MascarillaList(generics.ListCreateAPIView):
	queryset = Mascarilla.objects.all()
	serializer_class = MascarillaSerializer

class PedidoCreate(generics.CreateAPIView):
	queryset = Pedido.objects.all()
	serializer_class = PedidoSerializer

