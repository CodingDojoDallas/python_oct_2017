# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def environment(**options):
    env = Environment(**options)
    env.globals.update({
       'static': staticfiles_storage.url,
       'url': reverse,
    })
    return env

def index(request):
    # response = "placeholder to later display all the list of blogs"
    return render(request,'blogs_app/index.html')

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        print "*"*50
    return redirect("/")

def show(request, num):
    response = "placeholder to display blog {}".format(num)
    return HttpResponse(response)

def edit(request, num):
    response = "placeholder to edit blog {}".format(num)
    return HttpResponse(response)

def destroy(request, num):
    return redirect(r'/')
