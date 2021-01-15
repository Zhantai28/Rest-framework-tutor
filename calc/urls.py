from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'calc'
urlpatterns = [
    path('create/', CurrencyCreateView.as_view()),
    path('all/', CurrencyListView.as_view()),
    path('detail/<int:pk>/', CurrencyDetailView.as_view())
]
