from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'random_word/word.html')    

def generate(request):
    if request.method == "POST":
        request.session['random_string'] = get_random_string(length=14)
        if 'counter' not in request.session:
            request.session['counter'] = 1
        else:
            request.session['counter'] += 1
    return redirect('/')

def reset(request):
    if request.method == "POST" and 'counter' in request.session:
        del request.session['counter']
    return redirect('/')