from django.db import models
from django.urls import reverse


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    next_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    archive=models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('delete', kwargs={'id': self.id})

