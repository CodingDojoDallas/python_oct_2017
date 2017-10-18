from __future__ import unicode_literals

from django.db import models

class MrManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['name']) < 6:
            errors['name'] = "Course name must be greater than 5 characters."
        if len(data['desc']) < 16:
            errors['desc'] = "Course description must be greater than 15 characters."
        return errors;

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrManager()
