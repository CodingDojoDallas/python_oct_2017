from __future__ import unicode_literals
from django.db import models
from ..users.models import *

class MrBookManager(models.Manager):
    def book_validator(self, data):
        errors = {}
        if len(data['author']) < 2 or len(data['author']) > 45:
            errors['authorlen'] = "Author name must be between 2 and 45 characters."
        if not data['author'].replace(' ','').replace('-','').replace('.','').isalpha():
            errors['authorchars'] = "Author names can only contain letters and spaces."
        if len(data['title']) < 1 or len(data['title']) > 255:
            errors['titlelen'] = "Titles must be between 1 and 255 characters."
        if not data['title'].replace(' ','').replace("'", "").isalnum():
            errors['titlechars'] = "Titles can only contain letters, spaces, and numbers."
        return errors

    def create_book(self, data):
        book = self.create(title=data['title'], author=data['author'])
        return book

class MrReviewManager(models.Manager):
    def review_validator(self, data):
        errors = {}
        if len(data['review']) < 1:
            errors['review'] = "Review may not be blank."
        if data['stars'] < 1 or data['stars'] > 5 or not isinstance(data['stars'], int):
            errors['stars'] = "Sorry, you can't manipulate these. You may only give 1-5 stars."
        return errors

    def create_review(self, review, book, userid):
        reviewer = User.objects.get(id=userid)
        review = self.create(text=review['review'], stars=review['stars'], book=book, reviewer=reviewer)

    def delete_review(self, reviewid):
        if not self.filter(id=reviewid).exists():
            return False
        bookid = self.get(id=reviewid).book.id
        self.get(id=reviewid).delete()
        return bookid

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrBookManager()

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MrReviewManager()