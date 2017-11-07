from django import forms
from django.contrib.auth.models import  User

from .models import Perfil

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password',)

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ('direccion', 'telefono')
