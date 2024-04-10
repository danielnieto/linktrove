from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def remove_protocol(url):
    if "://" in url:
        return url.split("://", 1)[1]
    return url
