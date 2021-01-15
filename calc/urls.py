from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'calc'
urlpatterns = [
    path('calc/create/', CurrencyCreateView.as_view())
]
