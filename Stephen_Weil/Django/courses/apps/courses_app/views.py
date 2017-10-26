from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(req):
    return render(req, 'courses_app/index.html', {'courses': Course.objects.all()})

def add(req):
    if req.method == "POST":
        d = req.POST
        errors = Course.objects.validator(d)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            Course.objects.create(name=d['name'], desc=d['desc'])
    return redirect('/')

def destroy(req, courseid):
    return render(req, 'courses_app/delete.html', {'course': Course.objects.get(id=courseid)})

def delete(req, courseid):
    Course.objects.get(id=courseid).delete()
    return redirect('/')