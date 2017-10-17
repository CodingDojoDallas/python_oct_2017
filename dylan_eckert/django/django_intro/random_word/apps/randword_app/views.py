# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    # response = "placeholder to later display all the list of blogs"
    return render(request,'randword_app/index.html')
def create(request):
    if request.method == "POST":
        request.session['random_word'] = get_random_string(length=14)
        request.session['count'] += 1
    return redirect("/")
