from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import *

class ForumManager(models.Manager):
    def validate(self, post):
        errors = {}

        for key, val in post.items():
            if len(val) < 1:
                errors[key] = '{} cannot be empty'.format(key.replace('_',' ').title())

        return errors

    def postMessage(self, post, user_id, send_id):
        new = Message.objects.create(text = post['message'])
        recipients = User.objects.filter(id = user_id)
        recipient = recipients[0]
        new.recipients.add(recipient)
        sender = User.objects.get(id = send_id)
        new.senders.add(sender)

    def postComment(self, post, message_id, send_id):
        messages = Message.objects.filter(id = message_id)
        message = messages[0]
        new = Comment.objects.create(content = post['comment'], message = message)
        sender = User.objects.get(id = send_id)
        new.commenters.add(sender)

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    senders = models.ManyToManyField(User, related_name='sent_messages')
    recipients = models.ManyToManyField(User, related_name='received_messages')
    objects = ForumManager()
    def __str__(self):
        return 'Message:{}'.format(self.text)
    def __repr__(self):
        return 'Message:{}'.format(self.text)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)    
    message = models.ForeignKey(Message, related_name='comments')
    commenters = models.ManyToManyField(User, related_name='replies')
    objects = ForumManager()