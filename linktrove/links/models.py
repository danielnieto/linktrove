from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django_extensions.db.fields import ShortUUIDField

PLACEHOLDER_IMAGE_URL = "https://placehold.co/400x400?text={text}"


class Link(TimeStampedModel, TitleDescriptionModel, models.Model):
    id = ShortUUIDField(primary_key=True)
    notes = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    favicon = models.URLField(blank=True, null=True)
    url = models.URLField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    @property
    def thumbnail_or_default(self):
        if self.thumbnail:
            return self.thumbnail

        return PLACEHOLDER_IMAGE_URL.format(text=self.title.replace(" ", "+"))
