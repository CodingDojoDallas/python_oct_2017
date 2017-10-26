from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This app only exists to test stuff in the shell.')
