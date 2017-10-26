from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime
from time import strftime, localtime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

class UserManager(models.Manager):
    def login(self, post):
        users = self.filter(email = post['email'].lower())
        if len(users):
            user = users[0]
            if bcrypt.checkpw(post['password'].encode(), user.password.encode()):
                return user

        return False

    def validate(self, post, user_id=0):
        errors = {}
        for key, val in post.items():
            if len(val) < 1:
                errors[key] = '{} cannot be empty'.format(key.replace('_',' ').title()) 

        if 'first_name' not in errors and 'first_name' in post and not post['first_name'].isalpha():
            errors['first_name'] = 'First name should contain only alphabets'

        if 'last_name' not in errors and 'last_name' in post and not post['last_name'].isalpha():
            errors['last_name'] = 'Last name should contain only alphabets'

        if 'email' not in errors and 'email' in post and not re.match(EMAIL_REGEX, post['email'].lower()):
            errors['email'] = 'Invalid email address entered'

        if 'password' not in errors and 'password' in post and (len(post['password']) < 8 or not re.match(PASSWORD_REGEX, post['password'])):
            errors['password'] = 'Password must be at least 8 characters and contain a digit and capital letter'
        elif 'password' not in errors and 'password' in post and post['password'] != post['password_confirmation']:
            errors['password'] = 'Passwords do not match'

        if not len(errors.keys()) and 'email' in post:
            if len(self.filter(email = post['email'].lower()).exclude(id=user_id)) > 0:
                errors['email'] = 'Email address already in use'

        return errors
    
    def createUser(self, post):
        if not len(self.all()):
            admin = True
        else:
            admin = False
        if 'desc' not in post:
            desc = 'New to the land!'
        return self.create(
            first_name = post['first_name'],
            last_name = post['last_name'],
            email = post['email'].lower(),
            password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt()),
            desc = desc,
            admin = admin
        )
        
    def isAdmin(self, user_id):
        return self.filter(id = user_id)[0].admin

    def updateUser(self, post, user_id):
        user = User.objects.get(id = user_id)        
        if 'email' in post:
            user.email = post['email']
            user.first_name = post['first_name']
            user.last_name = post['last_name']
        elif 'password' in post:
            user.password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
        else:
            user.desc = post['desc']
        user.save()
        

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    desc = models.TextField()
    password = models.CharField(max_length = 255)    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    admin = models.BooleanField()
    objects = UserManager()
    def __repr__(self):
        return 'User:{} {}'.format(self.first_name, self.last_name)
    def __str__(self):
        return 'User:{} {}'.format(self.first_name, self.last_name)
 