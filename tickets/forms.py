from django import forms

from . import models


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = "__all__"
