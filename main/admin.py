from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "original_url", "short_url", "visits")
    list_display_links = ("id", "short_url", "visits")


admin.site.register(Link, LinkAdmin)