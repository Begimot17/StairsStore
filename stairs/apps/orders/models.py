from enum import Enum

from django.db import models

from accsuppliers.models import Supplier
from accclients.models import Client


class OrderClient(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    numlayers = models.IntegerField()
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
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    archive = models.BooleanField(default=False)

    order_number = models.CharField(max_length=200)
    order_date = models.DateField(null=True)
    approval_date = models.DateField(null=True)
    address = models.CharField(max_length=200)
    departure_date = models.DateField(null=True)
    estimated_price = models.IntegerField(null=True)
    final_price = models.IntegerField(null=True)
    install_date = models.DateField(null=True)
    num_days = models.IntegerField(null=True)
    complete_date = models.DateField(null=True)
    status = models.CharField(max_length=200)
    archive=models.BooleanField(default=False)

    def get_status_value(self):
        for st in StatusOrderClient:
            if self.status==st.name:
                return st.value


class StatusOrderClient(Enum):
    A = "Заплановано"
    B = "Затверджено"
    C = "Погоджено"
    D = "Установка"
    E = "Завершено"
    F = "Відхилено"
    G = "Перенесено"

class OrderSupplier(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=200)
    order_date = models.DateField(null=True)
    price = models.IntegerField()
    complete_date = models.DateField(null=True)
    phone = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    mark = models.CharField(null=True,max_length=200)
    archive=models.BooleanField(default=False)


    def get_supplier_name(self):
        return self.supplier.name
    def get_contact(self):
        return self.supplier.first_name+" "+self.supplier.last_name



class StatusOrderSupplier(Enum):
    A = "Замовлено"
    B = "Відправлено"
    C = "Отримано"
