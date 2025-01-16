from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dev/login/', views.dev_login, name='dev_login'),
    path('des/login/', views.des_login, name='des_login'),
    path('dev/register/', views.dev_register, name='dev_register'),
    path('des/register/', views.des_register, name='des_register'),
]