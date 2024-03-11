from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Update the list_display, fieldsets, and add_fieldsets to include custom fields
    list_display = ['email', 'username', 'status', 'is_staff', ]
    # fieldsets and add_fieldsets go here...
