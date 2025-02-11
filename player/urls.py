from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brower/', views.brower, name='brower'),
    path('detail/', views.detail, name='detail'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='profile-update'),
]
