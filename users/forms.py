from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField(max_length=30, required=True)
    lastName = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()
    phoneNumber = forms.CharField(max_length=9, required=True)
    department = forms.CharField(max_length=10, required=True)
    major = forms.CharField(max_length=15, required=True)
    semester = forms.IntegerField(required=True)
    aboutMe = forms.CharField(max_length=200, required=False)


    class Meta:
        model = User
        fields = ['username', 'firstName', 'lastName', 'email', 'phoneNumber', 'department', 'major', 'semester',
                  'aboutMe', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None  # Remove help text



