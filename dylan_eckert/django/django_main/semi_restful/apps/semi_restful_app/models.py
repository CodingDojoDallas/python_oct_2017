from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate(self, form_data):
        print "validating {}".format(form_data)
            #implement validations here

        return False

    def create_user(self, form_data):
        user = self.create(   # This is method for the user variable at views.py line#26
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
        )
        return user # will get returned to the user variable at views.py line#26

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True) # Will post Date&Time one time once created
    updated_at = models.DateTimeField(auto_now=True)  # Will post new Date&Time everytime it is updated

    objects = UserManager()   # This is telling it to go look for the methods I created

    def __repr__(self):      # Or use __str__(self)

        return "{} - {}".format(self.id, self.email) # .format() method will return the id and email of the user
# you can add "-" ( between {} {} ) make's it neat looking   // now you are ready to make your database
