from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tickets.models import Ticket
from reviews.models import Review
from tickets.forms import TicketForm
from reviews.forms import ReviewForm
from feeds.views import home


@login_required
def create_review(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            # user field is required (foreign key)
            ticket_form.instance.user = request.user
            ticket_form.save()

        # review_form = ReviewForm(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        image = request.FILES.get('image')
        ticket = Ticket(title=title, description=description, user=user, image=image)
        rating = request.POST["rating"]
        headline = request.POST["headline"]
        body = request.POST["body"]
        context = {"ticket": ticket, "rating": rating, "user": user, "headline": headline, "body": body}
        review = Review(ticket=ticket, rating=rating, user=user, headline=headline, body=body)
        review.save()
        return render(request, "reviews/create.html", context=context)

    else:
        ticket_form = TicketForm(initial={"user": request.user})
        review_form = ReviewForm(initial={"user": request.user})
        return render(request, "reviews/create.html", context={"ticket_form": ticket_form, "review_form": review_form})


@login_required
def update_review(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = get_user(request)
        image = request.FILES.get('image')
        ticket = Ticket(title=title, description=description, user=user, image=image)
        ticket.full_clean()
        ticket.save()
        rating = request.POST.get('rating')
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        review = Review(ticket=ticket, rating=rating, user=user, headline=headline, body=body)
        review.full_clean()
        review.save()
        return home(request)
    return render(request, 'reviews/update.html', context)
