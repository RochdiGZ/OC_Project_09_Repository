from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tickets.models import Ticket
from reviews.models import Review
from subscriptions.models import UserFollows

STARS = [1, 2, 3, 4, 5]


@login_required
def feed(request):
    # On sélectionne l'utilisateur et les personnes suivies
    user = get_user(request)
    followed_users = [pair.followed_user for pair in UserFollows.objects.filter(user=user)]
    user_posts = []
    user_posts.extend(followed_users)
    user_posts.append(user)
    elements = []
    # On recherche les tickets et reviews souhaitées
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    for user_post in user_posts:
        ticket_posts = Ticket.objects.filter(user=user_post)
        review_posts = Review.objects.filter(user=user_post)
        for review in review_posts:
            elements.append(review)
        for ticket in ticket_posts:
            elements.append(ticket)
    # On recherche les reviews des non abonnés
    user_tickets = Ticket.objects.filter(user=user)
    for ticket in user_tickets:
        review_user_tickets = Review.objects.filter(ticket=ticket)
        for review in review_user_tickets:
            if review not in elements:
                elements.append(review)
    # On trie par ordre chronologique
    sorted_list = sorted(elements, key=lambda x: x.time_created, reverse=True)
    # On recherche les reviews de l'utilisateur
    user_review = Review.objects.filter(user=user)
    # On crée une liste de tickets déjà critiqués par l'utilisateur
    tickets_stop_btn = [review.ticket for review in user_review]
    context = {
        'elements': sorted_list,
        'tickets_stop_btn': tickets_stop_btn,
        'tickets': tickets,
        'reviews': reviews,
        'followed_users': user_posts,
        'stars': STARS
    }
    return render(request, 'feeds/feed.html', context)
