from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime

from accclients.models import Client
from orders.models import StatusOrderClient, OrderClient


def index(request):
    clients= Client.objects.all()
    return render(request, 'controls/conorders.html',{'clients': clients})

def client(request,name):
    user = User.objects.get(username=name)
    cli = Client.objects.get(user_id=user.id)
    clients = Client.objects.all()
    return render(request, 'controls/conorders.html', {'clients': clients,'cli':cli})
def add(request):
    order = OrderClient(
        client_id=Client.objects.get(id=request.POST['clientid']),
        numlayers=request.POST['numlayers'],
        stair=request.POST['stair'],
        karkas=request.POST['karkas'],
        material=request.POST['material'],
        rail=request.POST['rail'],
        rail_material=request.POST['rail_material'],
        width=request.POST['width'],
        long=request.POST['long'],
        height=request.POST['height'],
        height_step=request.POST['height_step'],
        obrobka=request.POST['obrobka'],
        address=request.POST['address'],
        color=request.POST['color'],
        price=request.POST['price']
    )
    order.save()
    order.order_number = "ЗК" + str(order.id).zfill(6)
    order.order_date = datetime.date.today()
    order.address = request.POST['address']
    order.estimated_price = request.POST['price']
    order.status = StatusOrderClient.A.name
    order.save()

    return HttpResponseRedirect(reverse('conorders:index'))

