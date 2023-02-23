from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import forms


def create_ticket(request):
    if request.method == "POST":
        form = forms.CreateTicketForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(request.path)
    else:
        form = forms.CreateTicketForm()
    return render(request, "tickets/create.html", context={"form": form})
