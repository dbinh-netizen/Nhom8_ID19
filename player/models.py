from django.db import models
from django.contrib.auth.models import User  # Kết nối với model User có sẵn của Django

class Profile(models.Model):
    # Liên kết đến model User của Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Trường avatar để lưu ảnh đại diện người dùng
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    # Hàm trả về tên người dùng để hiển thị
    def __str__(self):
        return self.user.username
