from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    context = {
        "time": datetime.now()
    }
    return render(request, 'displayApp/index.html', context)            
