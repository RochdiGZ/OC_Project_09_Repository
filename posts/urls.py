from django.urls import path
from .views import edit_posts
urlpatterns = [
    path("", edit_posts, name="posts"),
]