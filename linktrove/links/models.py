from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django_extensions.db.fields import ShortUUIDField


class Link(TimeStampedModel, TitleDescriptionModel, models.Model):
    id = ShortUUIDField(primary_key=True)
    notes = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    url = models.URLField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.url
