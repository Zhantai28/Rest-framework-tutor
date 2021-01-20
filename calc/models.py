from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Currency(models.Model):
    first_curr = models.CharField(verbose_name='Валюта 1', max_length=5)
    first_qnt = models.CharField(verbose_name='Кол-во 1', max_length=65)
    second_curr = models.CharField(verbose_name='Валюта 1', max_length=5)
    second_qnt = models.CharField(verbose_name='Кол-во 2', max_length=65)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
