# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    data = {
        'users': User.objects.all()
    }
    print data
    return render(request, 'user_login/index.html', data)

def create(request):
    user = User.objects.create(first_name="Bob", last_name="Bobbers", email_address="bob@bob.com", age=45)
    print user.first_name, user.last_name, user.email_address, user.age
    return redirect('/')
