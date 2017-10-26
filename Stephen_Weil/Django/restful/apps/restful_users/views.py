from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(req):
    return render(req, 'restful_users/index.html', {'users': User.objects.all()})

def show(req, userid):
    return render(req, 'restful_users/user.html', {'user': User.objects.get(id=userid)})

def add(req):
    return render(req, 'restful_users/add.html')

def create(req):
    if req.method == "POST":
        d = req.POST
        errors = User.objects.validator(d)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
            return redirect('/users/add')
        else:
            User.objects.create(first_name=d['first'], last_name=d['last'], email=d['email'])
    return redirect('/users')

def edit(req, userid):
    return render(req, 'restful_users/edit.html', {'user': User.objects.get(id=userid)})

def update(req, userid):
    if req.method == "POST":
        print "in here"
        d = req.POST
        errors = User.objects.validator(d)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
            url = '/users/' + userid + '/edit'
            return redirect(url)
        else:
            user = User.objects.get(id=userid)
            user.first_name = d['first']
            user.last_name = d['last']
            user.email = d['email']
            user.save()
    return redirect('/users')

def delete(req, userid):
    User.objects.get(id=userid).delete()
    return redirect('/users')