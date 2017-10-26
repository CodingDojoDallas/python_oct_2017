from django.shortcuts import render, redirect

def index(request):
    return render(request, 'words/index.html')

def addWord(request):
    data = {
        'word':request.POST['word'],
        'color':request.POST['color'],
    }
    if 'size' in request.POST:
        data['size'] = request.POST['size']
    else:
        data['size'] = 'small'

    if 'words' not in request.session:
        request.session['words'] = []

    request.session['words'] += [data]
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')