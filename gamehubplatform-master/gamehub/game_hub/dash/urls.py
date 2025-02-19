from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.urls import path, include
urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('login/', views.login_view, name='login'),  # Trang đăng nhập
    path('register/', views.register, name='register'),  # Trang đăng ký
    path('playerhome/', views.player, name='player'),
    path('game/<str:index>',view=views.play,name="playgame"),
    path('player/', include('player.urls')),
]