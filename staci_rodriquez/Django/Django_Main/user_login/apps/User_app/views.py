from __future__ import unicode_literals
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Go make some shell queries")



# Create your views here.
