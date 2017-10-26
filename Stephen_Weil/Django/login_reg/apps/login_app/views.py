from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(req):
    return render(req, 'login_app/index.html')

def success(req):
    if 'id' in req.session:
        return render(req, 'login_app/success.html', {'user_info': User.objects.get(id=req.session['id'])})
    else:
        return redirect('/')

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
            req.session['status'] = 'register'
            return redirect('/success')
    return redirect('/')

def login(req):
    if req.method == "POST":
        d = req.POST
        if EMAIL_REGEX.match(d['email']):
            res = User.objects.login(d)
            if res['status']:
                req.session['id'] = res['user'].id
                req.session['status'] = 'login'
                return redirect('/success')
            else:
                for tag, error in res['errors'].iteritems():
                    messages.error(req, error, extra_tags=tag)
    return redirect('/')

def logout(req):
    req.session.clear()
    return redirect('/')