from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class MrManager(models.Manager):
    def validator(self, data):
        errors = {}
        first = data['first']
        last = data['last']
        if len(first) < 2 or len(last) < 2 or len(first) > 45 or len(last) > 45:
            errors['namelen'] = "Name must be between two and 45 characters."
        if not first.isalpha() or not last.isalpha():
            errors['namechars'] = "Names can only contain letters."
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

    def validate_desc(self, data):
        errors = {}
        if len(data['desc']) < 5:
            errors['desc'] = "Try harder. Description must be at least 5 characters."
        return errors

    def update_desc(self, data, userid):
        if self.filter(id=userid).exists():
            user = self.get(id=userid)
            user.desc = data['desc']
            user.save()
            return user
        else:
            return False

    def validate_pw(self, data):
        errors = {}
        if len(data['pword']) < 8:
            errors['pwlen'] = "Password must be at least 8 characters."
        if data['pword'] != data['conf']:
            errors['pwconf'] = "Password did not match confirmation."
        return errors

    def update_pw(self, data, userid):
        if self.filter(id=userid).exists():
            user = self.get(id=userid)
            user.pword = data['pword']
            user.save()
            return user
        else:
            return False

    def validate_info(self, data, userid):
        errors = {}
        first = data['first']
        last = data['last']
        if len(first) < 2 or len(last) < 2 or len(first) > 45 or len(last) > 45:
            errors['namelen'] = "Name must be between two and 45 characters."
        if not first.isalpha() or not last.isalpha():
            errors['namechars'] = "Names can only contain letters."
        if not EMAIL_REGEX.match(data['email']) or len(data['email']) > 255:
            errors['email'] = "Not a valid email."
        if not errors:
            if self.exclude(id=userid).filter(email=data['email']).exists():
                errors['email'] = "Email already taken."
        return errors

    def update_info(self, data, userid):
        if self.filter(id=userid).exists():
            user = self.get(id=userid)
            user.email = data['email']
            user.first = data['first']
            user.last = data['last']
            user.save()
            return user
        else:
            return False

    def create_user(self, data):
        if not self.all().exists():
            level = 1
        else:
            level = 0
        user = self.create(first=data['first'], last=data['last'], email=data['email'], level=level, pword=bcrypt.hashpw(data['pword'].encode(), bcrypt.gensalt()))
        return user

    def login(self, data):
        if self.filter(email=data['email']).exists():
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
    level = models.IntegerField()
    desc = models.TextField(default="No description added.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrManager()