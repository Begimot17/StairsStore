from datetime import datetime

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from excel_response import ExcelResponse

from .models import Supplier


def index(request):
    suppliers = Supplier.objects.all()
    return render(request, 'controls/accsuppliers.html', {'suppliers': suppliers})


def add(request):
    supplier = Supplier(name=request.POST['name'],
                        material=request.POST['material'],
                        category=request.POST['category'],
                        last_name=request.POST['last_name'],
                        first_name=request.POST['first_name'],
                        next_name=request.POST['next_name'],
                        email=request.POST['email'],
                        address=request.POST['address'],
                        phone=request.POST['phone']
                        )
    supplier.save()
    print(request.POST['name'])
    return HttpResponseRedirect(reverse('accsuppliers:index'))


def archive(request, id):
    supplier=Supplier.objects.get(id=id)
    if not supplier.archive:
        supplier.archive=True
    else:
        supplier.archive = False
    supplier.save()
    return HttpResponseRedirect(reverse('accsuppliers:index'))
def delete(request, id):
    Supplier.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('accsuppliers:index'))
def update(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.name = request.POST["name"]
    supplier.last_name = request.POST['last_name']
    supplier.first_name = request.POST['first_name']
    supplier.next_name = request.POST['next_name']
    supplier.email = request.POST["email"]
    supplier.address = request.POST['address']
    supplier.phone = request.POST['phone']
    supplier.category = request.POST['category']
    supplier.material = request.POST['material']
    supplier.save()
    return HttpResponseRedirect(reverse('accsuppliers:index'))
def excel(request):
    data = [
        ['Постачальник',
         'Категория',
         'Матеріал',
            'Прізвіще',
         'Імя',
         'По батькові',
         'Email',
         'Телефон',
         'Адреса',
         ],
    ]
    clients = Supplier.objects.all()
    for client in clients:
        data.append([client.name,
                     client.category,
                     client.material,
                     client.last_name,
                     client.first_name,
                     client.next_name,
                     client.email,
                     client.phone,
                     client.address,
                     ])
    return ExcelResponse(data, 'Suppliers'+str(datetime.now()))
