from django import forms

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre"}
        # widgets = {"title": forms.TextInput(attrs={"placeholder": "Titre", "label": ""})}
