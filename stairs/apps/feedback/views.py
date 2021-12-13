from django.shortcuts import render
from .models import Feedback
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'feedback.html')


def insert(request):
    feedback = Feedback(
        name=request.POST['name'],
        phone=request.POST['phone'],
        address=request.POST['address'],
        message=request.POST['message']
    )
    feedback.save()
    return HttpResponseRedirect(reverse('main:index'))