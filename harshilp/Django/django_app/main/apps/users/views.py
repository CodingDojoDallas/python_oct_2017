from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to list of all users")

def register(request):
    return HttpResponse("placeholder for form to create a new user record")
    
def login(request):
    return HttpResponse('placeholder for user login')

