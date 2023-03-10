from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur : ")
    password = forms.CharField(max_length=63, label="Mot de passe : ")

    class Meta:
        model = models.CustomUser
        fields = ["username", "password"]
