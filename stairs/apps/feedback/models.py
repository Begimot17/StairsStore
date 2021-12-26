from django.db import models
from enum import Enum


class StatusOrderClient(models.Model):
    name = models.CharField(max_length=50)
    # A = "Запланированно"
    # B = "Утверждено"
    # C = "Соглашено"
    # D = "Установка"
    # E = "Завершено"
    # F = "Отклонено"
    # G = "Перенесён"


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    status = models.ForeignKey(StatusOrderClient, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(null=True)
