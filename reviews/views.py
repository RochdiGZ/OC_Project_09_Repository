from django.shortcuts import render


def create_review(request):
    return render(request, "reviews/create_review.html")

