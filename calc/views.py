from rest_framework import generics
from .serializers import CurrencySerializer, CurrencyListSerializer
from .models import Currency


class CurrencyCreateView(generics.CreateAPIView):
    serializer_class = CurrencySerializer


class CurrencyListView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()


class CurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()