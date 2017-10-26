from django.shortcuts import render, redirect
from .models import *
from django.contrib.messages import error

#=================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ Renders ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=================================================================

def index(request):
    return render(request, 'login_reg/index.html')

def login(request):
    return render(request, 'login_reg/login.html')

def register(request):
    return render(request, 'login_reg/register.html')

#=================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~ Processes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=================================================================

def loginProcess(request):
    user = User.objects.login(request.POST)
    if user:
        request.session['user_id'] = user.id
        print request.session['user_id']
        return redirect('/dashboard')
    
    error(request, 'Invalid email or password')
    return redirect('/login')

def registerProcess(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for key, message in errors.iteritems():
            error(request, message, extra_tags=key)
        return redirect('/register')
    else:
        user = User.objects.createUser(request.POST)
        request.session['user_id'] = user.id
        return redirect('/dashboard')
