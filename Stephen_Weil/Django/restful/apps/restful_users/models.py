from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class MrManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['first']) < 2 or len(data['last']) < 2:
            errors['name'] = "First and last name must each be at least 2 characters."
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email was not valid."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrManager()