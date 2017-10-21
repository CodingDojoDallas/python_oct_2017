from django.shortcuts import render, redirect
from django.contrib.messages import error
from .models import User

# Create your views here.
def index(request):
    data = {
        'users':User.objects.all()
    }
    return render(request, 'users/index.html', data)

def new(request):
    return render(request, 'users/new.html')

def create(request):
    errors = User.objects.validation(request.POST)
    if len(errors):
        for key, message in errors.iteritems():
            error(request, message, extra_tags=key)
        return redirect('/users/new')
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/users/{}'.format(user.id))

def show(request, user_id):
    data = {
        'user':User.objects.get(id=user_id)
    }
    return render(request, 'users/show.html', data)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')

def edit(request, user_id):
    data = {
        'user':User.objects.get(id=user_id)
    }
    return render(request, 'users/edit.html', data)

def update(request, user_id):
    errors = User.objects.validation(request.POST)
    if len(errors):
        for key, message in errors.iteritems():
            error(request, message, extra_tags=key)
        return reidrect('/users/{}/edit'.format(user_id))
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users')
    



