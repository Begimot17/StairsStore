from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url('feedback/', views.feedback, name='feedback'),
    url('calculator/', views.calculator, name='calculator'),
    url('gallery/', views.gallery, name='gallery'),
    url('about/', views.about, name='about'),
    url('', views.index, name='index'),

]
