from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(blank=True, verbose_name="Photo de profil", upload_to="")


"""
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=63)
    password = models.CharField(max_length=63)
    profile_photo = models.ImageField(blank=True, verbose_name="Photo de profil", upload_to="")
"""