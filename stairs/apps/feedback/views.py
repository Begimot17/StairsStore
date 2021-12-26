from django.shortcuts import render
from .models import Feedback, StatusOrderClient
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


def index(request):
    feedbacks = Feedback.objects.all()
    print(feedbacks)
    return render(request, 'feedback.html')


def select(request):
    feedbacks = Feedback.objects.all()
    status = StatusOrderClient.objects.all()
    return render(request, 'feedback-list.html', {"feedbacks": feedbacks, "status": status})


def insert(request):
    feedback = Feedback(
        name=request.POST['name'],
        phone=request.POST['phone'],
        address=request.POST['address'],
        status_id=StatusOrderClient.objects.first().id,
        date=datetime.now(),
        message=request.POST['message']
    )
    feedback.save()
    return HttpResponseRedirect(reverse('main:index'))


def update(request, id):
    feedback = Feedback.objects.get(id=id)
    print(feedback.status)
    feedback.status = StatusOrderClient.objects.get(id=request.POST['status'])
    print(feedback.status)
    print(StatusOrderClient.objects.get(id=request.POST['status']))
    feedback.save()
    return HttpResponseRedirect(reverse('feedback:select'))
