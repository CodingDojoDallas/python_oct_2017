from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default="No Description Added")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "Book object - {} - {} - created: {}".format(self.name, self.desc, self.created_at)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    notes = models.TextField(default="No Notes Added")
    books = models.ManyToManyField(Book, related_name = "authors")
    def __repr__(self):
        return "Author object - {} {} - {} - {} - created: {}".format(self.first_name, self.last_name, self.email, self.notes, self.created_at)
