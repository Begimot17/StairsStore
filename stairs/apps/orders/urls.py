from django.urls import path
from .import views

app_name = 'orders'

urlpatterns = [
    path('suppliers', views.suppliers, name='suppliers'),
    path('c_del/<int:id>/', views.c_del,name='c_del'),
    path('c_cli/<str:order_number>/', views.c_cli,name='c_cli'),
    path('c_upd/<int:id>/', views.c_upd,name='c_upd'),
    path('c_arc/<int:id>/', views.c_arc,name='c_arc'),
    path('s_del/<int:id>/', views.s_del,name='s_del'),
    path('sup/<int:id>/', views.sup,name='sup'),
    path('s_upd/<int:id>/', views.s_upd,name='s_upd'),
    path('s_arc/<int:id>/', views.s_arc,name='s_arc'),
    path('clients', views.clients, name='clients'),
    path('client/<str:name>/', views.client, name='client'),
    path('addsuppliers', views.addsuppliers, name='addsuppliers'),
    # path('add', views.add,name='add'),
]
