from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('insert/', views.insert, name='insert'),
    path('select/', views.select, name='select'),
    path('update/<int:id>/', views.update, name='update'),
    path('', views.index, name='index'),
]
