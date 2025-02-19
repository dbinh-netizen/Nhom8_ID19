from django.contrib import admin
from django.urls import path
from . import views
from .views import game_detail, submit_review
urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('game/<int:game_id>/review/', submit_review, name='submit_review'),

]
