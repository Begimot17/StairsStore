from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    message = models.CharField(max_length=200)