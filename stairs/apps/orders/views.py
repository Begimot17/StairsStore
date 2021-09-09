import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from accsuppliers.models import Supplier
from .models import OrderClient, OrderSupplier, StatusOrderSupplier, StatusOrderClient
from accclients.models import Client



def s_del(request, id):
    OrderSupplier.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('orders:suppliers'))
def s_arc(request, id):
    order=OrderSupplier.objects.get(id=id)
    if not order.archive:
        order.archive=True
    else:
        order.archive = False
    order.save()
    return HttpResponseRedirect(reverse('orders:suppliers'))
def s_upd(request, id):
    order = OrderSupplier.objects.get(id=id)
    order.supplier_id=request.POST["supplier_id"]
    if not request.POST["order_date"] == "":
        order.order_date = datetime.datetime.strptime(request.POST["order_date"], '%Y-%m-%d')
    order.price = request.POST["price"]
    if not request.POST["complete_date"] == "":
        order.complete_date = datetime.datetime.strptime(request.POST["complete_date"], '%Y-%m-%d')
    order.phone = request.POST["phone"]
    order.status = request.POST["status"]
    order.mark = request.POST["mark"]
    order.save()
    return HttpResponseRedirect(reverse('orders:suppliers'))
def c_del(request, id):
    OrderClient.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('orders:clients'))
def c_arc(request, id):
    order=OrderClient.objects.get(id=id)
    if not order.archive:
        order.archive=True
    else:
        order.archive = False
    order.save()
    return HttpResponseRedirect(reverse('orders:clients'))
def c_cli(request, order_number):
    order=OrderClient.objects.get(order_number=order_number)
    status = list(StatusOrderClient)
    return render(request, 'controls/orderclient.html',
                  {"order": order,"status": status})

def c_upd(request, id):
    order = OrderClient.objects.get(id=id)
    order.status = request.POST["status"]
    if not request.POST["final_price"] == "":
        order.final_price = request.POST['final_price']
    if not request.POST["order_date"] == "":
        order.order_date = request.POST['order_date']
    if not request.POST["approval_date"] == "":
        order.approval_date = request.POST['approval_date']
    if not request.POST["departure_date"] == "":
        order.address = request.POST['departure_date']
    if not request.POST["departure_date"] == "":
        order.departure_date = request.POST['departure_date']
    if not request.POST["estimated_price"] == "":
        order.estimated_price = request.POST['estimated_price']
    if not request.POST["install_date"] == "":
        order.install_date = request.POST['install_date']
    if not request.POST["complete_date"] == "":
        order.complete_date = request.POST['complete_date']
    if not request.POST["num_days"] == "":
        order.num_days = request.POST["num_days"]
    order.save()
    return HttpResponseRedirect(reverse('orders:clients'))
def clients(request):
    orders= OrderClient.objects.all()
    status= list(StatusOrderClient)
    return render(request, 'controls/ordersclients.html',{"orders":orders,"status":status})
def client(request,name):
    user=User.objects.get(username=name)
    client=Client.objects.get(user_id=user.id)
    orders=OrderClient.objects.filter(client_id=client)
    status= list(StatusOrderClient)

    return render(request, 'controls/ordersclients.html',{"orders":orders,"status":status})
def suppliers(request):
    orders = OrderSupplier.objects.all()
    status= list(StatusOrderSupplier)
    suppliers = Supplier.objects.all()
    return render(request, 'controls/orderssuppliers.html',{"orders":orders,"suppliers":suppliers,"status":status})
def addsuppliers(request):
    supplier=Supplier.objects.get(id=request.POST['supplier_id'])
    order = OrderSupplier(
        order_number=request.POST['order_number'],
        supplier_id=request.POST['supplier_id'],
        order_date=datetime.date.today(),
        price=request.POST['price'],
        phone=supplier.phone,
        status=StatusOrderSupplier.A.value,
        mark=request.POST['mark']
    )
    order.save()
    return HttpResponseRedirect(reverse('orders:suppliers'))
def sup(request,id):
    supplier = Supplier.objects.get(id=id)
    return render(request, 'controls/supplier.html', {"order": supplier})
