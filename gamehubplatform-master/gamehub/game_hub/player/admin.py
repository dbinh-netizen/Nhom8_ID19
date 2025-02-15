from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# admin.site.register(DesignerProfile)
# admin.site.register(SystemAdminProfile)
# admin.site.register(PlayerProfile)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': ( 'fullname', 'role', 'email', 'phone', 'birthday', 'address', 'gender','img')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )

    list_display = ('id', 'username', 'fullname', 'role', 'email', 'phone', 'birthday', 'address', 'gender', 'is_active')
admin.site.register(CustomUser, CustomUserAdmin)