from django.shortcuts import render, redirect
from datetime import datetime
from random import randrange
# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['log'] = []
        request.session['debt'] = 'no'
    
    if int(request.session['gold']) < 0:
        request.session['debt'] = 'yes'
    elif int(request.session['gold']) > 100:
        request.session['debt'] = 'nah'
    else:
        request.session['debt'] = 'no'
    return render(request, 'ninjaGold/index.html')

def process(request):
    time = datetime.now()
    if request.POST['building'] == 'farm':
        val = randrange(10,21)
        request.session['log'] += [('Earned {} gold from the {}! {}'.format(val, request.POST['building'], time))]
        request.session['gold'] += val
    elif request.POST['building'] == 'cave':
        val = randrange(5,11)
        request.session['log'] += [('Earned {} gold from the {}! {}'.format(val, request.POST['building'], time))]
        request.session['gold'] += val
    elif request.POST['building'] == 'house':
        val = randrange(2,6)
        request.session['log'] += [('Earned {} gold from the {}! {}'.format(val, request.POST['building'], time))]
        request.session['gold'] += val
    elif request.POST['building'] == 'casino':
        luck = randrange(0,5)
        val = randrange(0,51)
        if luck != 2: 
            request.session['log'] += [('Lost {} gold from the {}! {}'.format(val, request.POST['building'], time))]
            request.session['gold'] -= val
        else:
            request.session['log'] += [('Earned {} gold from the {}! {}'.format(val, request.POST['building'], time))]            
            request.session['gold'] += val
    return redirect('/')