from PIL import Image
from LITReview import settings
from django.db import models
# from django_resized import ResizedImageField


class Ticket(models.Model):
    IMAGE_MAX_SIZE = (300, 300)
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null=True, blank=True)
    # image = ResizedImageField(size=[200, 300], quality=100, force_format='JPEG', null=True, blank=True, upload_to='')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()

    def __str__(self):
        return f"{self.title} | {self.user}"
