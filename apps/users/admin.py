from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'name',
                'email',
                'gender',
                'age',
                'phone',
                'is_staff',
            )
        }),
    )
    list_display = (
        'id',
        'username',
        'name',
        'email',
        'gender',
        'age',
        'phone',
        'date_joined',
        'last_login',
        "is_active",
        "is_staff",
        "is_superuser",
    )

# admin page 로그인 기록
class UserLoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent',)
    list_filter = ('ip_address',)
    date_hierarchy = 'created'

admin.site.register(models.UserLoginLog, UserLoginLogAdmin)
