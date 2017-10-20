# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# pre-populated an items list in products.py
from products import items
from django.shortcuts import render, redirect


def index(request):
    
    # clear out last_transaction from session, so as not to make it seem like we are
    # charging user multiple times when they view this page
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']

    context = {
        "items": items
    }
    return render(request, 'store/index.html', context)

def buy(request, item_id):

    # find item in our items list from the url's item_id matching the 'id' key on the item
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    # handle exceptions for session keys if they do not yet exist
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0        

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')