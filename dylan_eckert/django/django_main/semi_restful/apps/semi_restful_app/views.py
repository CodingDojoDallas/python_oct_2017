from django.shortcuts import render, redirect, reverse
from .models import User

def index(request):
    print "Inside the index method"  # Print where you are to locate where the data flow is at
    
    context={         # passing users to html page with context (dictionary)
    'users': User. objects.all()
    }

    return render(request, 'semi_restful_app/index.html', context) #add context here so that it expects it
#This will render (GET) the index.html file from templates (index.html)

def new(request):   # Setup the route named NEW
    print "Inside the new method"   # Print where you are to locate where the data flow is at

    return render (request, 'semi_restful_app/new.html')
#This will render (GET) the new.html file from templates (new.html)

def create(request): #This method is made to define the url (named route) made in URL.PY
    print "Inside the create method" # Print where you are to locate where the data flow is at
    if request.method == "POST":
        pass
    # NEXT WE NEED TO VALIDATE
        errors = User.objects.validate(request.POST) # Make a method inside the USERMANAGER called .validate()
# calling validate and passing the information you got inside request.post
        # if errors exits
        
        if errors:
            pass # flash the errors

        # create user if no errors are made
        user = User.objects.create_user(request.POST) #  Now we have to create a create_user method
 
# Need to pass data through a Kwargs method // reverse() method is expecting data through it
        
        return redirect( reverse('show_user', kwargs={'id': user.id }) )


    return redirect(reverse('new_user')) # reverse our variable for new user
# reverse() is a method that lets you use named routes inside the back-end
# if they send informatio that is not right they will be sent back to the form

def show(request, id):  # need to add 'id', to pass data (the id ) through it

    user = User.objects.get(id = id) # gettting the data

    context = {     # Getting the data to show w/ a dictionary
        'user' : user, # user key equal to the user
    }

    return render(request, 'semi_restful_app/show.html', context)
# Requesting an html page from that specific app ALSO with the context