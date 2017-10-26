from django.shortcuts import render, redirect
from .models import *
from ..books.models import *
from django.contrib import messages

def index(req):
    return render(req, 'users/index.html')

def register(req):
    if req.method == "POST":
        d = req.POST
        errors = User.objects.validator(d)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            user = User.objects.create_user(d)
            req.session['id'] = user.id
            return redirect('/books')
    return redirect('/')

def login(req):
    if req.method == "POST":
        d = req.POST
        if EMAIL_REGEX.match(d['email']):
            res = User.objects.login(d)
            if res['status']:
                req.session['id'] = res['user'].id
                return redirect('/books')
            else:
                for tag, error in res['errors'].iteritems():
                    messages.error(req, error, extra_tags=tag)
        else:
            messages.error(req, 'Login information invalid.', extra_tags="login")
    return redirect('/')

def userpage(req, userid):
    if 'id' not in req.session:
        return redirect('/')
    if not User.objects.filter(id=userid).exists():
        return redirect('/books')
    context = {
        'user': User.objects.get(id=userid)
    }
    context['reviews'] = Review.objects.filter(reviewer=context['user'])
    context['books'] = Book.objects.filter(reviews__in=context['reviews'])
    return render(req, 'users/user.html', context)

def logout(req):
    req.session.clear()
    return redirect('/')