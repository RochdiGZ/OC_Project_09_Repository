from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_photo = models.ImageField(blank=True, upload_to="", verbose_name="Photo de profil")
