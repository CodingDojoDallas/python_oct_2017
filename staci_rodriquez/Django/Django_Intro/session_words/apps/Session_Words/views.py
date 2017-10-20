from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []

    return render(request, 'Session_Words/index.html')

def add_word(request):
    new_word = {}

    new_word['color'] = request.POST['color'] if 'color' in request.POST else ""
    new_word['content'] = request.POST['content'] 
    new_word['big'] = 'big' if 'show-big' in request.POST else ""
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")

    request.session['words'] += [new_word]

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
        
        # Create your views here.
