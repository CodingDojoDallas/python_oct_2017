from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import random

def index(request):
    return render(request,'random_word/index.html')

def randomword(request):
    if 'counter' in request.session:     #check to see if counter in request.session // this will let us count how many time the user has reset a new random word
        request.session['counter'] += 1
    else:                                # if not in session set the session to counter += 1 // 
        request.session['counter'] = 1

    word = ''  # Here we are creating an empty word// we will use this to insert letters to it below

    my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for times in range (0, 24):   # for whatever in the range(start, stop) (talking about the list)
        word = word + str(random.choice(my_letters))  #The empty word is word+= a string which is random.choice of my

    words = {            #dictionary of words with random_word as a key word and "word" as a value
        'random_word': word
    }
    return render(request, 'random_word/index.html', words) 

def reset(request):
    request.session.clear()   # the clear() built-in method will clear out the session
    return redirect('/')
    
     
    
   
