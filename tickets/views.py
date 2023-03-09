import os
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from tickets.models import Ticket
from reviews.models import Review
from feeds.views import feed


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            # user field is required (foreign key)
            form.instance.user = request.user
            form.save(commit=True)
            return HttpResponseRedirect(request.path)  # return HttpResponseRedirect(reverse("feed"))
    else:
        form = forms.TicketForm()
    return render(request, "tickets/create.html", context={"form": form})


@login_required
def update_ticket(request, ticket_id=""):
    context = {}
    if ticket_id:
        ticket = Ticket.objects.get(id=ticket_id)
        context["ticket"] = ticket
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = get_user(request)
        image = request.FILES.get("image")
        # Cas où l'on va modifier un ticket existant
        if ticket_id:
            ticket = Ticket.objects.get(id=ticket_id)
            ticket.title = title
            ticket.description = description
            if image:
                if ticket.image:
                    ticket.image.close()
                    os.remove(ticket.image.path)
                ticket.image = image
        # Cas où l'on crée un nouveau ticket
        else:
            ticket = Ticket(title=title, description=description, user=user, image=image)
        ticket.full_clean()
        ticket.save()
        return feed(request)
    return render(request, 'tickets/update.html', context)


@login_required
def reply_ticket(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id)[0]
    context = {'ticket': ticket}
    user = get_user(request)
    test_review = Review.objects.filter(ticket=ticket, user=user)
    if test_review:
        context['actual_review'] = test_review[0]
    if request.method == "POST":
        user = get_user(request)
        rating = request.POST.get('rating')
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        # Cas de modification de review
        if test_review:
            test_review[0].rating = rating
            test_review[0].headline = headline
            test_review[0].body = body
            test_review[0].full_clean()
            test_review[0].save()
        # Cas de création de review
        else:
            review = Review(rating=rating, headline=headline, body=body, user=user, ticket=ticket)
            review.full_clean()
            review.save()
        return feed(request)

    return render(request, 'tickets/reply.html', context)
