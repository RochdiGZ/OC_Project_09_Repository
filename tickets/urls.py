from django.urls import path, re_path
from .views import create_ticket, update_ticket, reply_ticket

urlpatterns = [
    path("create", create_ticket, name="create-ticket"),
    path("update", update_ticket, name="update-ticket"),
    re_path(r"^update-ticket(?:/(?P<ticket_id>[0-9]+)/)?$", update_ticket, name="update-ticket"),
    path("reply/<ticket_id>", reply_ticket, name="reply-ticket"),
]
