# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "<Blog object: fname:{} lname:{} email:{} age:{} crat:{} uat:{}>".format(self.first_name, self.last_name, self.email_address, self.age, self.created_at, self.updated_at)
