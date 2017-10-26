from django.shortcuts import render, HttpResponse, redirect
import random
import string



# Create your views here.
def index(request):
    if not 'count' in request.session:
            request.session['count'] = 0
    if not 'string' in request.session:
            request.session['string'] = ' '

    return render(request,'index.html')

# Generates session values if not existing
def create(request):
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    request.session['string'] = random_string
    request.session['count'] += 1
    return redirect('/')
