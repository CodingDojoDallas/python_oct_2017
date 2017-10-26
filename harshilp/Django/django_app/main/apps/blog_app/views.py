from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Placeholder to blog list"
    return HttpResponse(response)

def new(request):
    response = 'Placeholder for form to create new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/')

def showBlog(request, blog_id):
    response = 'Placeholder for blog number {}'.format(blog_id)
    return HttpResponse(response)

def edit(request, blog_id):
    response = 'Placeholder to edit blog {}'.format(blog_id)
    return HttpResponse(response)

def delete(request, blog_id):
    return redirect('/blogs')
