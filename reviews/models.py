from django.core.validators import MinValueValidator, MaxValueValidator

from LITReview import settings
from django.db import models


class Review:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    rating = models.PositiveSmallIntegerField(max_length=1024,
                                              validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
