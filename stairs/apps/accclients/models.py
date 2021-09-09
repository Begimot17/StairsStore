from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    next_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    num_orders=0
    archive=models.BooleanField(default=False)
