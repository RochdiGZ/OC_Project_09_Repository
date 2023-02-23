from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import forms


def create_review(request):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(request.path)
    else:
        form = forms.CreateReviewForm()

    return render(request, "reviews/create.html", context={"form": form})
