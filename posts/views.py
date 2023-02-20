from django.shortcuts import render


def edit_posts(request):
    return render(request, "posts/edit_posts.html")
