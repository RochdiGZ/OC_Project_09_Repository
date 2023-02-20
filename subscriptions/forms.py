from django import forms


class SubscribersForm(forms.Form):
    # https://docs.djangoproject.com/en/4.1/ref/forms/fields/
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
