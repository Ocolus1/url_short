from django.db import models
from datetime import datetime
import string
from random import choices

class Link(models.Model):
    original_url = models.CharField(max_length=250)
    short_url = models.CharField(max_length=100, unique=True)
    visits = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)
        if self.short_url:
            pass
        else:
            self.short_url = self.generate_short_link()


    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = "".join(choices(characters, k=4))

        link = Link.objects.filter(short_url=short_url)

        if link:
            return self.generate_short_link()

        return short_url

    def __str__(self):
        return self.original_url

