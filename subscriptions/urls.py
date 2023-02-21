from django.urls import path
from .views import subscribers
urlpatterns = [
    path("", subscribers, name="subscribers"),
]
