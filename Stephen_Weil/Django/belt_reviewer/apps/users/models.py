from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class MrManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['name']) < 2 or len(data['name']) > 45:
            errors['namelen'] = "Name must be between 2 and 45 characters."
        if not data['name'].replace(' ','').isalpha():
            errors['namechars'] = "Names can only contain letters."
        if len(data['alias']) < 2 or len(data['alias']) > 45:
            errors['aliaslen'] = "Alias must be between 2 and 45 characters."
        if not data['alias'].isalnum():
            errors['aliaschars'] = "Alias must only contain alphanumeric characters."
        if not EMAIL_REGEX.match(data['email']) or len(data['email']) > 255:
            errors['email'] = "Not a valid email."
        if len(data['pword']) < 8:
            errors['pwlen'] = "Password must be at least 8 characters."
        if data['pword'] != data['conf']:
            errors['pwconf'] = "Password did not match confirmation."
        if not errors:
            if self.filter(email=data['email']).exists():
                errors['email'] = "Email already taken."
        return errors

    def create_user(self, data):
        user = self.create(name=data['name'], email=data['email'], alias=data['alias'], pword=bcrypt.hashpw(data['pword'].encode(), bcrypt.gensalt()))
        return user

    def login(self, data):
        errors = {}
        if self.filter(email=data['email']).exists():
            user = self.get(email=data['email'])
            if bcrypt.checkpw(data['pword'].encode(), user.pword.encode()):
                return {'status': True, 'user': user}
            else:
                errors['login'] = "Login information invalid."
        else:
            errors['login'] = "Login information invalid."
        return {'status': False, 'errors': errors}

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    pword = models.CharField(max_length=255)
    alias = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrManager()
