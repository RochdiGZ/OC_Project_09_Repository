from LITReview import settings
from django.db import models


class Ticket(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"

    def __str__(self):
        return self.title
