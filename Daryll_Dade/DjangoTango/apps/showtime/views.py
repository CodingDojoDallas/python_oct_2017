from django.shortcuts import render, HttpResponse
import datetime
def firstview(request):
    context = {
        "time": datetime.datetime.now('%B %S %Y %w %S %p ')
    }

    return render(request,'page.html', context)
