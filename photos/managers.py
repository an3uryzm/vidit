from django.db import models
from django.apps import apps


class PhotoQuerySet(models.QuerySet):
    pass


class PhotoManager(models.Manager):
    def get_queryset(self):
        return PhotoQuerySet(self.model, using=self._db)
