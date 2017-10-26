from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "User object - {} {} - {} - created: {}".format(self.first_name, self.last_name, self.email, self.created_at)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, default="No description added.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    liked_users = models.ManyToManyField(User, related_name="liked_books")
    def __repr__(self):
        return "Book object - {} - {} - created: {}".format(self.name, self.desc, self.created_at)