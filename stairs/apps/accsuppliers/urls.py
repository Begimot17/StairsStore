from django.urls import path
from . import views

app_name = 'accsuppliers'

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('index', views.index, name='index'),
    path('add', views.add, name='add'),
    path('excel', views.excel, name='excel'),
    path('archive/<int:id>/', views.archive, name='archive'),
]
