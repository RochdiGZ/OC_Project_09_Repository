from django.shortcuts import render

from .forms import SubscribersForm


def subscribers(request):
    form = SubscribersForm()
    return render(request, "subscriptions/subscribers.html", context={"form": form})
