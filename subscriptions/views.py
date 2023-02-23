from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import forms


def subscribers(request):
    if request.method == "POST":
        form = forms.SubscribersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(request.path)
    else:
        form = forms.SubscribersForm()

    return render(request, "subscriptions/subscribers.html", context={"form": form})
