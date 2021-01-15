from rest_framework import generics
from .serializers import CurrencySerializer


class CurrencyCreateView(generics.CreateAPIView):
    serializer_class = CurrencySerializer
