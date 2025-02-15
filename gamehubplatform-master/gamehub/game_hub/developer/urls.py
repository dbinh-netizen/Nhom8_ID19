from django.urls import path
from .views import developer_dashboard, upload_game

urlpatterns = [
    path('dashboard/', developer_dashboard, name='developer_dashboard'),
    path('upload/', upload_game, name='upload_game'),
]