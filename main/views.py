from django.shortcuts import render, redirect
from .models import Link
from django.db.models import Count, Q


def stats(request):
    query_set = Link.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        query_set = query_set.filter(
            Q(original_url__icontains=query)
        ).distinct()

    context = {
        "query_set": query_set,
        "query": query
    }
    return render(request, "main/results.html", context)


def redirect_to_url(request, short_url):
    link = Link.objects.get(short_url=short_url)

    link.visits += 1
    link.save()

    return redirect(link.original_url)


def index(request):
    return render(request, "main/index.html", {})


def add_link(request):

    if request.method == "POST":
        original_url = request.POST["original_url"]
        link = Link.objects.create(original_url=original_url)

    context = {
        "new_link": link.short_url,
        "original_url": link.original_url
    }

    return render(request, "main/link_added.html", context)


def search(request):

    return render(request, "main/stats.html")
