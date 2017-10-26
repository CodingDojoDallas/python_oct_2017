from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(req):
    return render(req, 'users/index.html')

def signin(req):
    return render(req, 'users/signin.html')

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
            req.session['level'] = user.level
            req.session['status'] = 'register'
            return redirect('/dashboard')
    req.session['status'] = 'register'
    return redirect('/signin')

def create(req):
    if req.method == "POST":
        d = req.POST
        errors = User.objects.validator(d)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            user = User.objects.create_user(d)
            req.session['id'] = user.id
            req.session['level'] = user.level
            req.session['status'] = 'register'
            return redirect('/dashboard')
    return redirect('/users/new')

def edit(req, userid):
    if req.session['id'] != int(userid) and req.session['level'] != 1:
        return redirect('/dashboard')
    return render(req, 'users/edit.html', {'user': User.objects.get(id=userid)})

def login(req):
    if req.method == "POST":
        d = req.POST
        if EMAIL_REGEX.match(d['email']):
            res = User.objects.login(d)
            if res['status']:
                req.session['id'] = res['user'].id
                req.session['level'] = res['user'].level
                return redirect('/dashboard')
            else:
                for tag, error in res['errors'].iteritems():
                    messages.error(req, error, extra_tags=tag)
        else:
            messages.error(req, 'Login information invalid.', extra_tags="login")
    req.session['status'] = 'login'
    return redirect('/signin')

def logout(req):
    req.session.clear()
    return redirect('/signin')

def dashboard(req):
    if 'id' not in req.session:
        return redirect('/signin')
    return render(req, 'users/dashboard.html', {'users': User.objects.all()})

def addpage(req):
    if 'level' not in req.session or req.session['level'] == 0:
        return redirect('/dashboard')
    return render(req, 'users/addnew.html')

def update(req, userid):
    if 'id' not in req.session:
        return redirect('/signin')
    url = '/users/edit/' + userid
    if req.method == "POST":
        d = req.POST
        if 'desc' in d:
            errors = User.objects.validate_desc(d)
            if errors:
                messages.error(req, errors['desc'], extra_tags='desc')
            else:
                User.objects.update_desc(d, userid)
                messages.success(req, 'Description successfully updated!', extra_tags='desc')
        elif 'pword' in d:
            errors = User.objects.validate_pw(d)
            if errors:
                for tag, error in errors.iteritems():
                    messages.error(req, error, extra_tags=tag)
            else:
                User.objects.update_pw(d, userid)
                messages.success(req, 'Password successfully updated!', extra_tags='pword')
        elif 'email' in d:
            errors = User.objects.validate_info(d, userid)
            if errors:
                for tag, error in errors.iteritems():
                    messages.error(req, error, extra_tags=tag)
            else:
                User.objects.update_info(d, userid)
                messages.success(req, 'Profile info successfully updated!', extra_tags='profile')
    return redirect(url)