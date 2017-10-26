from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse('Placeholder to later display a list of all the blogs.')

def new(request):
    return HttpResponse('Placeholder to display a form to create a new blog.')

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse('Placeholder to display blog {}'.format(number))

def edit(request, number):
    return HttpResponse('Placeholder to edit blog {}'.format(number))

def destroy(request, number):
    return redirect('/blogs')
