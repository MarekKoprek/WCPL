from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
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
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None  # Remove help text



