# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def login(self, post):
        email = post['email'].lower()
        password = post['password']

        users = User.objects.filter(email=email)
        if len(users):
            user = users[0]
            if user.password == password:
                return user

        return False

    def userIsValid(self, post):
        email = post['email'].lower()
        password = post['password']
        cpassword = post['cpassword']

        errors = []
        # do all the email stuff like REGEX and shit IN THIS IF STATEMENT BELOW!!!!
        if len(email) < 6 or len(email) > 32:
             errors.append('Email has to be between 6-32 characters')

        if len(password) < 8 or len(password) > 255:
             errors.append('Password has to be between 5-255 characters')
        elif password != cpassword:
            errors.append('Passwords do not match')

        if not errors:
            users = self.filter(email = email)
            if users:
                errors.append('Email already taken')

        return {'status': len(errors) == 0, 'errors':errors}

    def newUser(self, post):
        email = post['email']
        password = post['password']
        return self.create(email = email, password = password)



class User(models.Model):
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=255)
    objects = UserManager()

    def __str__(self):
        return "email: {}".format(self.email)
