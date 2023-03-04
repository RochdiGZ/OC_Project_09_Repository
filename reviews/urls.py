from django.urls import path
from .views import create_review, update_review
urlpatterns = [
    path("create", create_review, name="create-review"),
    path("update", update_review, name="update-review"),
]
