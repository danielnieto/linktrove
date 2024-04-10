from django.contrib import admin
from .models import Link  # Import the Link model


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("url", "description", "created", "modified", "user")
    list_filter = ("created", "user")
    search_fields = ("url", "description", "user__email")
