from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(request.path)  # return HttpResponseRedirect(reverse("home"))
    else:
        form = forms.TicketForm()
    return render(request, "tickets/create.html", context={"form": form})
