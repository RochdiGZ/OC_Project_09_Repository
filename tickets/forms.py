from django import forms

from django.contrib.auth.forms import UserCreationForm

from tickets.models import Ticket


class TicketForm(forms.Form):
    title = forms.CharField(max_length=63, label="Titre : ")
    description = forms.CharField(max_length=63, label="Description : ")
    image = forms.ImageField(null=True, blank=True)


class CreateTicketForm(TicketForm):
    class Meta:
        model = Ticket
        fields = "__all__"
