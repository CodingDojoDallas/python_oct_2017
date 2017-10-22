from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class MrManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['first']) < 2 or len(data['last']) < 2:
            errors['namelen'] = "Name must be more than two characters."
        if not data['first'].isalpha() or not data['last'].isalpha():
            errors['namechars'] = "Names can only contain letters."
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Not a valid email."
        if len(data['pword']) < 8:
            errors['pwlen'] = "Password must be at least 8 characters."
        if data['pword'] != data['conf']:
            errors['pwconf'] = "Password did not match confirmation."
        return errors

    def create_user(self, data):
        user = self.create(first=data['first'], last=data['last'], email=data['email'], pword=bcrypt.hashpw(data['pword'].encode(), bcrypt.gensalt()))
        return user

    def login(self, data):
        user = self.get(email=data['email'])
        errors = {}
        if user:
            if bcrypt.checkpw(data['pword'].encode(), user.pword.encode()):
                return {'status': True, 'user': user}
            else:
                errors['login'] = "Login information invalid."
        else:
            errors['login'] = "Login information invalid."
        return {'status': False, 'errors': errors}

class User(models.Model):
    first = models.CharField(max_length=45)
    last = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    pword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrManager()