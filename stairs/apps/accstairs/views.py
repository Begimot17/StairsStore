from datetime import datetime

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Stair
from excel_response import ExcelResponse


def index(request):
    stairs = Stair.objects.all()
    return render(request, 'controls/accstairs.html', {'stairs': stairs})


def add(request):
    stair = Stair(
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
        color=request.POST['color'],
        price=request.POST['price']
                  )
    stair.save()
    print(request.POST['color'])
    return HttpResponseRedirect(reverse('accstairs:index'))

def delete(request, id):
    Stair.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('accstairs:index'))
def archive(request, id):
    stair=Stair.objects.get(id=id)
    if not stair.archive:
        stair.archive=True
    else:
        stair.archive = False
    stair.save()
    return HttpResponseRedirect(reverse('accstairs:index'))
def update(request, id):
    stair = Stair.objects.get(id=id)
    stair.stair = request.POST["stair"]
    stair.karkas = request.POST['karkas']
    stair.material = request.POST['material']
    stair.rail = request.POST['rail']
    stair.rail_material = request.POST['rail_material']
    # stair.width = request.POST['width'],
    # stair.long = request.POST['long'],
    # stair.height = request.POST['height'],
    # stair.height_step = request.POST['height_step'],
    stair.obrobka = request.POST['obrobka']
    stair.price = request.POST['price']
    stair.save()
    return HttpResponseRedirect(reverse('accstairs:index'))
def excel(request):
    data = [
        ['Вид матеріалу',
         'Тип каркасу',
         'Вид сходів',
         'Вид огорожі',
         'Вид матеріалу огорожі',
         'Вид обробки',
         'Колір сходи',
         'Сума в грн',
         ],
    ]
    stairs = Stair.objects.all()
    for stair in stairs:
        data.append([stair.material,
                     stair.karkas,
                     stair.stair,
                     stair.rail,
                     stair.rail_material,
                     stair.obrobka,
                     stair.color,
                     stair.price
                     ])
    return ExcelResponse(data, 'stairs'+str(datetime.now()))
