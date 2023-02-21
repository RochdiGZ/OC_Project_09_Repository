from django import forms

from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur : ")
    password = forms.CharField(max_length=63, label="Mot de passe : ")


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", )
