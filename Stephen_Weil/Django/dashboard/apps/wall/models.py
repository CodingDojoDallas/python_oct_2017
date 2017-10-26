from __future__ import unicode_literals

from django.db import models
from ..users.models import *

class MrPostManager(models.Manager):
    def validator(self, data, userid):
        errors = {}
        if len(data['text']) < 1:
            errors['post'] = "Posts may not be empty."
        if not User.objects.filter(id=userid).exists():
            errors['recipient'] = "That person does not exist."
        return errors

    def reply_validator(self, data, postid):
        errors = {}
        if len(data['text']) < 1:
            errors['reply'] = "Replies may not be empty."
        if not Post.objects.filter(id=postid).exists():
            errors['post'] = "That post does not exist."
        return errors

    def create_post(self, sender, data, userid):
        user = User.objects.get(id=sender)
        recipient = User.objects.get(id=userid)
        message = self.create(author=user, text=data['text'], recipient=recipient)
        return message

    def create_reply(self, sender, data, postid):
        author = User.objects.get(id=sender)
        post = Post.objects.get(id=postid)
        reply = self.create(author=author, text=data['text'], message=post)
        return reply

class Post(models.Model):
    author = models.ForeignKey(User, related_name="sent_messages")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipient = models.ForeignKey(User, related_name="rec_messages")
    objects = MrPostManager()

class Reply(models.Model):
    author = models.ForeignKey(User, related_name="sent_replies")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.ForeignKey(Post, related_name="replies")
    objects = MrPostManager()