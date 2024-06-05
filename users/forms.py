from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    TYPE = [
        ('1', 'Student account'),
        ('2', 'Firm account'),
    ]
    email = forms.EmailField()
    type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=TYPE,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None