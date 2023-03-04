from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from tickets.models import Ticket
from reviews.models import Review
import os

STARS = [1, 2, 3, 4, 5]


def edit_posts(request):
    elements = []
    actual_user = get_user(request)
    reviews = Review.objects.filter(user=actual_user)
    for review in reviews:
        elements.append(review)
    tickets = Ticket.objects.filter(user=actual_user)
    for ticket in tickets:
        elements.append(ticket)
    # Cas où l'utilisateur appuie sur le bouton Supprimer pour supprimer un ticket
    if 'ticket_delete' in request.POST:
        id_to_delete = request.POST.get('ticket_delete')
        ticket_to_delete = Ticket.objects.get(id=id_to_delete)
        if ticket_to_delete.image and os.path.exists(ticket_to_delete.image.path):
            os.remove(ticket_to_delete.image.path)
        ticket_to_delete.delete()
        return redirect('posts')
    # Cas où l'utilisateur appuie sur le bouton Supprimer pour supprimer une review
    if 'review_delete' in request.POST:
        id_to_delete = request.POST.get('review_delete')
        review_to_delete = Review.objects.get(id=id_to_delete)
        review_to_delete.delete()
        return redirect('posts')
    context = {
        'elements': sorted(elements, key=lambda x: x.time_created, reverse=True),
        'tickets': tickets,
        'reviews': reviews,
        'stars': STARS
    }

    return render(request, 'posts/edit_posts.html', context)
