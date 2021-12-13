from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'main'

urlpatterns = [
    url('calculator/', views.calculator, name='calculator'),
    url('portfolio/', views.portfolio, name='portfolio'),
    url('team/', views.team, name='team'),
    url('about/', views.about, name='about'),
    url('admin/', admin.site.urls, name='admin'),
    url('', views.index, name='index'),

]
