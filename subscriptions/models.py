from LITReview import settings
from django.db import models


class UserFollows(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user', )

        verbose_name = "Suivi"
