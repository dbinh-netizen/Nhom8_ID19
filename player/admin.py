from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, DesignerProfile, SystemAdminProfile


admin.site.register(DesignerProfile)
admin.site.register(SystemAdminProfile)