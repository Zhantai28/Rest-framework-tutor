from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'first_curr', 'first_qnt', 'second_curr', 'second_qnt')
