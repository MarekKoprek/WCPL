from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField()
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('firm', 'Firm'),
    )
    user_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=USER_TYPE_CHOICES,
    )

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2', 'user_type']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None


class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'faculty', 'course', 'semester', 'bio']

class FirmForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nameFirm', 'website', 'bio']