from django.shortcuts import render, redirect
import random
import datetime
from pytz import timezone
import pytz

def index(request):
    return render(request, 'ninja_gold/index.html')

def process(request, building):
    if 'total' not in request.session:
        request.session['total'] = 0
        request.session['activites'] = []
    functions = {
        'farm': lambda: random.randint(10,20),
        'cave': lambda: random.randint(5,10),
        'house': lambda: random.randint(2,5),
        'casino': lambda: random.randint(0,50) if random.random() >= .5 else random.randint(0,50)*(-1)
    }
    if building in functions:
        gold = functions[building]()
        request.session['total'] += gold
        if gold >= 0:
            message = {
                'text': "Earned " + str(gold) + " gold at the " + building + ".",
                'class': 'green'
            }
        else:
            message = {
                'text': "Lost " + str(gold*-1) + " gold at the casino.",
                'class': 'red'
            }
        central = timezone('US/Central')
        message['time'] = datetime.datetime.now(tz=pytz.utc).astimezone(central).strftime("%I:%M %p - %Y/%m/%d")
        request.session['activites'] += [message]
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')