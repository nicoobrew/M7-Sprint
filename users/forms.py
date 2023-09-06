from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

