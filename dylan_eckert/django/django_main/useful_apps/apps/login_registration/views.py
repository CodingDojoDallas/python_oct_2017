# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
# ===================================================
#                      VIEWS
# ===================================================

def index(req):
    return render(req, 'login_registration/index.html')

def home(req):
    if 'user_id' not in req.session:
        return redirect('/')

    users = User.objects.all()
    data = {'users': users}

    return render(req, 'login_registration/home.html', data)

# ===================================================
#                    PROCESSES
# ===================================================
def login(req):
    user = User.objects.login(req.POST)
    if user:
        req.session['user_id'] = user.id
        return redirect('/home')

    messages.error(req, 'Email or Password invalid')
    return redirect('/')

def registration(req):
    res = User.objects.userIsValid(req.POST)
    if res['status']:
        user = User.objects.newUser(req.POST)
        req.session['user_id'] = user.id
        return redirect('/home')
    else:
        for error in res['errors']:
            messages.error(req, error)

    return redirect('/')

def logout(req):
    req.session.clear()

    return redirect('/')
