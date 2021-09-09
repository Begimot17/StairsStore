from django.urls import path
from . import views

app_name = 'accclients'

urlpatterns = [
    path('archive/<int:id>', views.archive, name='archive'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('excel', views.excel, name='excel'),
    path('index', views.index, name='index'),
    path('add', views.add, name='add'),

]
