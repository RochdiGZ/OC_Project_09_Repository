from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    profile_photo = models.ImageField(blank=True, upload_to="", verbose_name="Photo de profil")
