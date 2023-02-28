from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from tickets.models import Ticket
from reviews.models import Review
from tickets.forms import TicketForm
from reviews.forms import ReviewForm


@login_required
def create_review(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket_form.save(commit=True)

        ticket = Ticket.objects.filter(user=request.user.latest("time_created"))
        rating = request.POST["rating"]
        user = request.user
        headline = request.POST["headline"]
        body = request.POST["body"]
        review = Review.objects.create(ticket, rating, user, headline, body)
        review_form = ReviewForm(review)
        review_form.save(commit=True)
        return HttpResponseRedirect(reverse("posts"))
    else:
        ticket_form = TicketForm(initial={"user": request.user})
        review_form = ReviewForm(initial={"user": request.user})
        return render(request, "reviews/create.html", context={"ticket_form": ticket_form, "review_form": review_form})
