from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistration(UserCreationForm):
    username = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserOurRegistration, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Имя*"
        self.fields['last_name'].label = "Фамилия*"
        self.fields['username'].label = "Адрес электронной почты"

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']