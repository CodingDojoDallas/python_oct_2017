from django.shortcuts import render, redirect

def index(request):
    if 'error' in request.session:
        del request.session['error']
    else:
        if 'error_message' in request.session:
            del request.session['error_message']
    return render(request, 'sales/index.html')

def purchase(request):
    if request.method == "POST":
        if 'items' not in request.session:
            request.session['items'] = 0
            request.session['total'] = 0
        quantity = int(request.POST['quantity'])
        item = request.POST['item']
        prices = {
            '1': 19.99,
            '2': 29.99,
            '3': 4.99,
            '4': 49.99
        }
        if item in prices:
            price = prices[request.POST['item']]
            request.session['items'] += quantity
            request.session['total'] += (price * quantity)
            request.session['charge'] = (price * quantity)
        else:
            request.session['message'] = "Nice try messing with our website. Now fuck right off."
        return redirect('/checkout')
    else:
        request.session['error_message'] = "Whatchu tryna do?"
        request.session['error'] = 1
        return redirect('/')

def checkout(request):
    return render(request, 'sales/checkout.html')