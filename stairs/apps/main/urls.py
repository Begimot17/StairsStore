from django.urls import path
from django.contrib import admin
from . import views

app_name = 'main'

urlpatterns = [
    path('calculator/', views.calculator, name='calculator'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),

]
