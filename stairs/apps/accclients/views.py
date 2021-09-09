from datetime import datetime

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from excel_response import ExcelResponse

from orders.models import OrderClient
from .models import Client


def index(request):
    clients = Client.objects.all()
    orders=OrderClient.objects.all()
    for client in clients:
        count=0
        for order in orders:
            if order.client_id.id == client.id:
                count+=1
        client.num_orders=count
    return render(request, 'controls/accclients.html', {'clients': clients})

def excel(request):
    data = [
        ['Прізвіще',
         'Імя',
         'По батькові',
         'Email',
         'Телефон',
         'Кількість замовленнь',
         ],
    ]
    orders=OrderClient.objects.all()
    clients = Client.objects.all()
    for client in clients:
        count=0
        for order in orders:
            if order.client_id.id == client.id:
                count+=1
        client.num_orders=count
    for client in clients:
        data.append([client.last_name,
                     client.first_name,
                     client.next_name,
                     client.email,
                     client.phone,
                     client.num_orders,
                     ])
    return ExcelResponse(data, 'Clients'+str(datetime.now()))
def add(request):
    client = Client(
        last_name=request.POST['last_name'],
        first_name=request.POST['first_name'],
        next_name=request.POST['next_name'],
        phone=request.POST['phone'],
        email=request.POST['email']
    )
    client.save()
    return HttpResponseRedirect(reverse('accclients:index'))

def archive(request, id):
    client=Client.objects.get(id=id)
    if not client.archive:
        client.archive=True
    else:
        client.archive = False
    client.save()
    return HttpResponseRedirect(reverse('accclients:index'))
def delete(request, id):
    Client.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('accclients:index'))

def update(request, id):
    client = Client.objects.get(id=id)
    client.last_name=request.POST['last_name']
    client.first_name=request.POST['first_name']
    client.next_name=request.POST['next_name']
    client.phone=request.POST['phone']
    client.email=request.POST['email']
    client.save()
    return HttpResponseRedirect(reverse('accclients:index'))
