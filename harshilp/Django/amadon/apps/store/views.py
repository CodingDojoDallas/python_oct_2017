from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0

    if 'products' not in request.session: 
        request.session['products'] = [
            {'id':1,'name':'Dojo T shirt','price':19.99},
            {'id':2,'name':'Dojo Sweater','price':29.99},
            {'id':3,'name':'Dojo Cup','price':4.99},
            {'id':4,'name':'Algo Book','price':49.99}
        ]
    print request.session['products']
    if 'sum' in request.session:
        del request.session['sum']

    return render(request, 'store/index.html')

def buy(request, product_id):
    request.session['sum'] = int(request.POST.get('quantity')) * request.session['products'][int(product_id) - 1]['price']
    request.session['total'] += request.session['sum']
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')

def goBack(request):
    del request.session['sum']
    return redirect('/')
