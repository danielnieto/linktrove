from taggit.forms import TagWidget
from django.forms import TextInput


class TagsWidget(TagWidget):
    template_name = "links/widgets/tags.html"


class URLWidget(TextInput):
    template_name = "links/widgets/url.html"
