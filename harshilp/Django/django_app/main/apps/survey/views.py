from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to list of all surveys")

def new(request):
    return HttpResponse("placeholder for users to create surveys")