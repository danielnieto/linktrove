from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from django_extensions.db.fields import ShortUUIDField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

PLACEHOLDER_IMAGE_URL = "https://placehold.co/400x400?text={text}"


class TaggedLink(TaggedItemBase):
    content_object = models.ForeignKey("Link", on_delete=models.CASCADE)


class Link(TimeStampedModel, TitleDescriptionModel, models.Model):
    id = ShortUUIDField(primary_key=True)
    notes = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    favicon = models.URLField(blank=True, null=True)
    url = models.URLField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager(through=TaggedLink, blank=True)

    def __str__(self):
        return self.url

    @property
    def thumbnail_or_default(self):
        if self.thumbnail:
            return self.thumbnail

        return PLACEHOLDER_IMAGE_URL.format(text=self.title.replace(" ", "+"))
