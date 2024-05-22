from django.contrib import admin
from .models import Profile, Event

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'faculty',
        'course',
        'semester',
        'bio'
    )

class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        #'users',
        'addDate',
        'startDate',
        'endDate',
        'title',
        'description'
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventsAdmin)