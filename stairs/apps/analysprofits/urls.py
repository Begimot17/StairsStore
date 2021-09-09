from django.urls import path
from . import views

app_name = 'analysprofits'

urlpatterns = [
    # path('delete/<int:id>/', views.delete,name='delete'),
    path('index', views.index, name='index'),
    # path('add', views.add,name='add'),
]
