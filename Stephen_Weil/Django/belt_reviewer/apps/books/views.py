from django.shortcuts import render, redirect
from .models import *
from ..users.models import *
from django.contrib import messages

def index(req):
    if 'id' not in req.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=req.session['id']),
        'reviews': Review.objects.all().order_by('-id')[:3],
        'books': Book.objects.all(),
        'range': range(5)
    }
    return render(req, 'books/index.html', context)

def addpage(req):
    if 'id' not in req.session:
        return redirect('/')
    books = list(Book.objects.all())
    authors = []
    for book in books:
        if book.author not in authors:
            authors.append(book.author)
    return render(req, 'books/add.html', {'authors': authors})

def create(req):
    if 'id' not in req.session:
        return redirect('/')
    if req.method == "POST":
        book = {
            'author': req.POST['author'] if len(req.POST['addauthor']) == 0 else req.POST['addauthor'],
            'title': req.POST['title']
        }
        # check if book info is valid
        errors = Book.objects.book_validator(book)
        if errors:
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            # check if review is valid
            review = {
                'review': req.POST['review'],
                'stars': int(req.POST['stars'])
            }
            errors = Review.objects.review_validator(review)
            if errors:
                for tag, error in errors.iteritems():
                    messages.error(req, error, extra_tags=tag)
            else:
                book = Book.objects.create_book(book)
                userid = req.session['id']
                review = Review.objects.create_review(review, book, userid)
                return redirect('/books')
    return redirect('/books/add')

def bookpage(req, bookid):
    if 'id' not in req.session:
        return redirect('/')
    # quick redirect if book doesn't exist
    if not Book.objects.filter(id=bookid).exists():
        return redirect('/books')
    book = Book.objects.get(id=bookid)
    context = {
        'book': book,
        'reviews': Review.objects.filter(book=book),
        'range': range(5)
    }
    return render(req, 'books/book.html', context)

def review(req, bookid):
    if 'id' not in req.session:
        return redirect('/')
    if req.method == "POST":
        # quick redirect if book doesn't exist
        if not Book.objects.filter(id=bookid).exists():
            return redirect('/books')
        review = {
            'review': req.POST['review'],
            'stars': int(req.POST['stars'])
        }
        errors = Review.objects.review_validator(review)
        if errors:
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            book = Book.objects.get(id=bookid)
            userid = req.session['id']
            review = Review.objects.create_review(review, book, userid)
    url = '/books/show/' + bookid
    return redirect(url)

def delete(req, reviewid):
    if 'id' not in req.session:
        return redirect('/')
    bookid = Review.objects.delete_review(reviewid)
    if bookid:
        url = '/books/show/' + str(bookid)
    else:
        url = '/books'
    return redirect(url)