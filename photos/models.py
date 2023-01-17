from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from .managers import PhotoManager

User = get_user_model()


class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='photos')
    description = models.TextField(blank=True)
    user_date = models.DateField(null=True)
    people_names = ArrayField(
        models.CharField(max_length=255),
        default=list,
        blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    objects = PhotoManager()
