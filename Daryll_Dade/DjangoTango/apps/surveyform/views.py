from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # context = {'myninja' : ninja

    }
     return render(request, "surveyform/index.html", context)
