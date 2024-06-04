from django import forms
from django.contrib.auth.models import User
from .models import Profile, Event

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'faculty', 'course', 'semester', 'bio']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['picture', 'title', 'description', 'startDate', 'endDate']
        
class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = []