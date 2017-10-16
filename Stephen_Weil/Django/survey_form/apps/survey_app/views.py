from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_app/form.html')

def process(request):
    if request.method == 'POST':
        if 'counter' not in request.session:
            request.session['counter'] = 1
        else:
            request.session['counter'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    if 'counter' in request.session:
        return render(request, 'survey_app/result.html')
    else:
        return redirect('/')