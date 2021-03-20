from django.urls import path
from .views import index, redirect_to_url, add_link, stats, search

app_name = "main"
urlpatterns = [
    path("", index, name="index"),
    path("short/<short_url>", redirect_to_url, name="short-url"),
    path("add_link", add_link, name="add-link"),
    path("stats", stats, name="stats"),
    path("search", search, name="search"),
]