from django.shortcuts import render, HttpResponse, redirect
import datetime
from pytz import timezone
import pytz

def index(request):
    # timezone in settings.py is set to UTC, so datetime.now() gets that rather
    # than local, using pytz to display CST
    central = timezone('US/Central')
    day = datetime.datetime.now(tz=pytz.utc).astimezone(central).strftime("%B %d, %Y")
    time = datetime.datetime.now(tz=pytz.utc).astimezone(central).strftime("%I:%M %p")
    context = {
        'day': day,
        'time': time,
        'zone': central
    }
    return render(request, 'time_display/time.html', context)
