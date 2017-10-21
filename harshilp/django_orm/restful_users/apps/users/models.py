from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validation(self, form_vals):
        errors = {}

        for key, val in form_vals.items():
            if len(val) < 1:
                errors[key] = '{} cannot be empty'.format(key.replace('_',' '))

        if 'email' not in errors and not re.match(EMAIL_REGEX, form_vals['email']):
            errors['email'] = 'Invalid email address'
        else:
            if len(self.filter(email = form_vals['email'])) > 0:
                errors['email'] = 'Email address already in use'

        return errors
 
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

