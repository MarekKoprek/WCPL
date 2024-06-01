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
        'addDate',
        'startDate',
        'endDate',
        'title',
        'description',
        'accepted'
    )
    filter_horizontal = ('users',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventsAdmin)