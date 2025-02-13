from django.urls import path
from . import views
<<<<<<< HEAD
=======
from .views import admin_dashboard, designer_dashboard, leaderboard, leaderboard_view, player_dashboard 
from django.urls import path
from .views import game_detail, submit_review
>>>>>>> code_cua_sang

urlpatterns = [
    path('', views.home, name='home'),
    path('brower/', views.brower, name='brower'),
    path('detail/', views.detail, name='detail'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='profile-update'),
<<<<<<< HEAD
]
=======
    path('dashboard/', player_dashboard, name='player_dashboard'),
    path('designer/dashboard/', designer_dashboard, name='designer_dashboard'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    

    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('game/<int:game_id>/review/', submit_review, name='submit_review'),
    path('leaderboard/<int:game_id>/', leaderboard, name='leaderboard'),
     path('leaderboard/', leaderboard_view, name='leaderboard'),
]


>>>>>>> code_cua_sang
