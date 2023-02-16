from django.shortcuts import render


def subscribers(request):
    return render(request, "subscriptions/subscribers.html")
