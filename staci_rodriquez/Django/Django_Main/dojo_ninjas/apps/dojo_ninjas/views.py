from django.shortcuts import render, redirect, reverse

def index(request):
    response = "Hello world!"
    return (response)
