from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profiles.models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
    )

    ordering = ['id']


admin.site.register(User, CustomUserAdmin)