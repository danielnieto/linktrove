import factory
from .models import Link


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Link

    url = factory.Faker("url")
    notes = factory.Faker("text")
    title = factory.Faker("sentence")
    description = factory.Faker("text")
