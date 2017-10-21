from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/results')

def results(request):
    print request.session['count']
    return render(request, 'survey/results.html')

def goBack(request):
    return redirect('/')