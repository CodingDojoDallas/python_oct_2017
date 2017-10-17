from django.shortcuts import render, redirect
import datetime
import pytz
from pytz import timezone

def index(request):
    return render(request, 'session_words/index.html')

def clear(request):
    request.session.clear()
    return redirect('/')

def add_word(request):
    if request.method == "POST":
        if 'words' not in request.session:
            request.session['words'] = []
        central = timezone('US/Central')
        def bigfont():
            if 'bigfont' in request.POST:
                return request.POST['bigfont']
            else:
                return None
        request.session['words'] += [{
            'word': request.POST['word'],
            'color': request.POST['radio'],
            'size': bigfont(),
            'day': datetime.datetime.now(tz=pytz.utc).astimezone(central).strftime("%B %d, %Y"),
            'time': datetime.datetime.now(tz=pytz.utc).astimezone(central).strftime("%I:%M %p")
            }]
        return redirect('/')