from django.contrib import admin
from .models import Profile, Event, Bug

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'bio')

    def get_fields(self, request, obj=None):
        fields = ['user', 'user_type', 'bio', 'picture']
        if obj:
            if obj.user_type == 'student':
                fields.extend(['phone_number', 'faculty', 'course', 'semester'])
            elif obj.user_type == 'firm':
                fields.extend(['nameFirm', 'website'])
        return fields
    

class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'picture',
        'addDate',
        'startDate',
        'endDate',
        'title',
        'description',
        'accepted'
    )
    filter_horizontal = ('users',)

class BugAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'section',
        'description'
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventsAdmin)
admin.site.register(Bug, BugAdmin)