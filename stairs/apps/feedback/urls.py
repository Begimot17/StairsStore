from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [
    url('insert/', views.insert, name='insert'),
    url('', views.index, name='index'),
]
