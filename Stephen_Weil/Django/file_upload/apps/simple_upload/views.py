from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'simple_upload/index.html')

def upload(request):
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        request.session['uploaded_file_url'] = fs.url(filename)
    return redirect('/')