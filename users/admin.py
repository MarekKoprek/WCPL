from django.contrib import admin

from django.contrib import admin
from .models import User  # Zaimportuj swój model User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'department', 'major', 'semester')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('department', 'major', 'semester')

admin.site.register(User, UserAdmin)
