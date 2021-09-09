from django.conf.urls import url
from . import views

app_name = 'authorize'

urlpatterns = [
    url('signin', views.signin, name='signin'),
    url('signup', views.signup, name='signup'),
    url('reg/', views.reg, name='reg'),
    url('log/', views.log, name='log'),
    url('log_out/', views.log_out, name='log_out'),
    # url('signup/', SignUpView.as_view(), name='signup'),
    url('getusers/', views.getusers, name='getusers'),
]
