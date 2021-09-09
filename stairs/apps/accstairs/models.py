from django.db import models
from django.urls import reverse


class Stair(models.Model):
    stair = models.CharField(max_length=200)
    karkas = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    rail = models.CharField(max_length=200)
    rail_material = models.CharField(max_length=200)
    height = models.IntegerField()
    width = models.IntegerField()
    long = models.IntegerField()
    height_step = models.IntegerField()
    obrobka = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.IntegerField()
    archive=models.BooleanField(default=False)
    def get_color_url(self):
        return "/assets/images/colors/{}.png".format(self.color)


