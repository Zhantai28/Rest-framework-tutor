from rest_framework import generics
from .serializers import CurrencySerializer


class CurrencyView(generics.CreateAPIView):
    serializer_class = CurrencySerializer