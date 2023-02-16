from django.shortcuts import render


def create_ticket(request):
    return render(request, "tickets/create_ticket.html")
