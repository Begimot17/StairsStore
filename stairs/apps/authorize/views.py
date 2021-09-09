from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from accclients.models import Client


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))


def reg(request):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    client= Client.objects.create(user=user,email=request.POST['email'],
                                  first_name=request.POST['first_name'],
                                  last_name=request.POST['last_name'])
    client.save()
    return HttpResponseRedirect(reverse('accounts:index'))


def log(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
    return HttpResponseRedirect(reverse('accounts:index'))


def getusers(request):
    a = User.objects.all()
    return render(request, 'registration/users.html', {'users': a})


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')
