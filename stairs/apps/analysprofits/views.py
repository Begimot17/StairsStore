from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import randrange
import json
from orders.models import OrderClient, OrderSupplier, StatusOrderClient


class Sup(object):
    def __init__(self, name, month, price):
        self.name = name
        self.month = month
        self.price = price
    def __str__(self):
        return self.name+" "+str(self.month)+" "+str(self.price)
class ListPrice(object):
    def __init__(self, name, price):
        self.name = name
        self.price = list
    def __str__(self):
        return self.name+" "+str(self.month)+" "+str(self.price)
def list_name(arr):
    ls=[]
    for a in arr:
        if a.name not in ls:
            ls.append(a.name)
    return ls

def list_month(arr):
    ls=[]
    for a in arr:
        if a.month not in ls:
            ls.append(a.month)
    return ls


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Sup):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
def index(request):
    sups = orders_sups()
    cli=orders_client()
    jsups = json.dumps(sups, ensure_ascii=False)
    jcli = json.dumps(cli, ensure_ascii=False)
    return render(request, 'controls/analysprofits.html',{'jsup': jsups,'jcli': jcli})

def orders_client():
    orders = OrderClient.objects.order_by('order_date')
    ords = []
    for ord in orders:
        if ord.status=="A" or ord.status=="B" or ord.status=="C" or ord.status=="D":
            ords.append(Sup(name='Замовлення виконується', month=ord.order_date.strftime("%m/%Y"), price=ord.price))
        elif ord.status=="E":
            ords.append(Sup(name='Виконані замовлення', month=ord.order_date.strftime("%m/%Y"), price=ord.price))

    sups = []
    for ord in ords:
        check = True
        for sup in sups:
            if sup.month == ord.month and sup.name == ord.name:
                sup.price += 1
                check = False
        if check:
            sups.append(Sup(name=ord.name,month=ord.month,price=1))
    data = [[""]]
    data[0].append('Виконані замовлення')
    data[0].append('Замовлення виконується')
    count = 0
    for month in list_month(sups):
        data.append([list_month(sups)[count]])
        count += 1
        for name in list_name(sups):
            check = True
            for sup in sups:
                if sup.month == month and sup.name == name:
                    data[count].append(sup.price)
                    check = False
                    break
            if check:
                data[count].append(0)
    print(data)
    return data

def orders_sups():
    orders = OrderSupplier.objects.order_by('order_date')
    ords = []
    for ord in orders:
        ords.append(Sup(name=ord.supplier.name,month=ord.order_date.strftime("%m/%Y"), price=ord.price))
    sups = []
    for ord in ords:
        check = True
        for sup in sups:
            if sup.month == ord.month and sup.name == ord.name:
                sup.price += ord.price
                check = False
                break
        if check:
            sups.append(ord)
    data = [[""]]
    for l in list_name(sups):
        data[0].append(l)
    count=0
    for month in list_month(sups):
        data.append([list_month(sups)[count]])
        count += 1
        for name in list_name(sups):
            check=True
            for sup in sups:
                if sup.month==month and sup.name==name:
                    data[count].append(sup.price)
                    check=False
                    break
            if check:
                data[count].append(0)
    print(data)
    return data
def profit():
    orders_sups = OrderSupplier.objects.order_by('order_date')
    ords = []
    for ord in orders_sups:
        ords.append(Sup(name=ord.supplier.name, month=ord.order_date.strftime("%m/%Y"), price=ord.price))
    sups = []
    for ord in ords:
        check = True
        for sup in sups:
            if sup.month == ord.month and sup.name == ord.name:
                sup.price += ord.price
                check = False
                break
        if check:
            sups.append(ord)
    orders_cli = OrderClient.objects.order_by('order_date')
    ords_cli = []
    for ord in orders_cli:
        if ord.status == "E":
            check = True
            for sup in sups:
                if sup.month == ord.month and sup.name == ord.name:
                    sup.price += ord.price
                    check = False
            if check:
                sups.append(Sup(name=ord.name, month=ord.month, price=ord.price))

    for ord in ords:
        check = True
        for sup in sups:
            if sup.month == ord.month and sup.name == ord.name:
                sup.price += ord.price
                check = False
                break
        if check:
            sups.append(ord)

    data = [[""]]
    data[0].append('Дохід')
    data[0].append('Витрата')
    data[0].append('Чистий прибуток')
    count = 0
    for month in list_month(sups):
        data.append([list_month(sups)[count]])
        count += 1
        for name in list_name(sups):
            check = True
            for sup in sups:
                if sup.month == month and sup.name == name:
                    data[count].append(sup.price)
                    check = False
                    break
            if check:
                data[count].append(0)
    print(data)
    return sups