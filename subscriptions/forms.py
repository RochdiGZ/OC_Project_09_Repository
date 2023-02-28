from django import forms

from . import models


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = "__all__"
        labels = {"user": "Utilisateur", "followed_user": "Utilisateur suivi"}
