from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(verbose_name="Bio", help_text="The bio of the author.", max_length=500)


class Journal(models.Model):
    title = models.CharField(verbose_name="Title", help_text="The title of the journal.", max_length=255)
    author = models.ForeignKey(Author)

class Page(models.Model):
    title = models.CharField(verbose_name="Title", help_text="The title of the page.", max_length=255)
    content = models.TextField(verbose_name="Content", help_text="The content of the page.")
    created_at = models.DateTimeField(verbose_name="Created at", help_text="The date and time the page was created.", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", help_text="The date and time the page was updated.", auto_now=True)
    author = models.ForeignKey(Author)
    journal = models.ForeignKey(Journal)
