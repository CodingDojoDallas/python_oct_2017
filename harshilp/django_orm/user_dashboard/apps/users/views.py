from django.shortcuts import render, redirect
from ..login_reg.models import *
from .models import *
from django.contrib.messages import error

#=================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Renders ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=================================================================

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    elif User.objects.isAdmin(request.session['user_id']):
        request.session['admin'] = True
    data = {
        'users': User.objects.all()
    }
    return render(request, 'users/dashboard.html', data)

def show(request, user_id):
    data = {
        'user':User.objects.get(id=user_id),
    }
    return render(request, 'users/show.html', data)

def new(request):
    pass


def edit(request):
    if not 'user_id' in request.session:
        return redirect('/login')
    else:
        data = {
            'user': User.objects.get(id = request.session['user_id'])
        }
    return render(request, 'users/edit.html', data)

def editAdmin(request, user_id):
    if not 'admin' in request.session:
        return redirect('/dashboard')
    pass

#=================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~ Processes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=================================================================

def post(request, user_id):
    errors = Message.objects.validate(request.POST)
    if len(errors):
        for key, message in errors.iteritems():
            error(request, message, extra_tags=key)
    else:
        Message.objects.postMessage(request.POST, user_id, request.session['user_id'])
    return redirect('/users/show/{}'.format(user_id))

def comment(request, user_id, message_id):
    errors = Comment.objects.validate(request.POST)
    if len(errors):
        for key, message in errors.iteritems():
            error(request, message, extra_tags=key)
    else:
        Comment.objects.postComment(request.POST, message_id, request.session['user_id'])
    return redirect('/users/show/{}'.format(user_id))

def editProfile(request):
    errors = User.objects.validate(request.POST, request.session['user_id'])
    if len(errors):
        for key, message in errors.iteritems():
            error(request, message, extra_tags=key)
        return redirect('/users/edit')
    else:
        User.objects.updateUser(request.POST, request.session['user_id'])
    return redirect('/users/show/{}'.format(request.session['user_id']))

def logoff(request):
    request.session.clear()
    return redirect('/')