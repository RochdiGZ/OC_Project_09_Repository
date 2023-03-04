from django.core.validators import MinValueValidator, MaxValueValidator

from tickets.models import Ticket
from LITReview import settings
from django.db import models


class Review(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Critique"

    def __str__(self):
        return f"Critique du ticket {self.ticket} par {self.user}"
