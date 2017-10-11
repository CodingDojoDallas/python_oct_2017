import re
from flask import flash, Flask, render_template, request, redirect   # Import Flask and the class of render_template, request and redirect
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    # Gthis creates an instance of the flask class
app.secret_key = 'KeepItSecretKeepItSafe'                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which says yo, listen for the route
                        #If you ever hit this route, then run that function and do some shit
                        # if you ever have /something/<SOMETHINGELSE>, the somethingelse gets stored in a variable and you put it into the variable of what it is
def takeIndex():        #if you do that, then you HAVE to put the variable into the function to pass in
    return render_template('index.html')  #this is grabbing the html page, and assigning the name and the version to have some values
#render template is a function that literally renders a template

@app.route('/submit', methods=['POST'])
def submit():

    errors = False

    content = {
        "firstname": str(request.form['firstname']),
        "lastname": str(request.form['lastname']),
        "email": request.form['email'],
        "birthdate": request.form['birthdate'],
        "password": request.form['password'],
        "confirmpassword": request.form['confirmpassword']
    }

    if len(content["firstname"]) < 1:
        flash("First name cannot be empty")
        errors = True
    if str.isalpha(content["firstname"]) != True:
        flash("Your first name can't have a number")
        errors = True
    if len(content['lastname']) < 1:
        flash("Last name cannot be empty")
        errors = True
    if str.isalpha(content["lastname"]) != True:
        flash("Your last name can't have a number")
        errors = True
    if len(content['email']) < 1:
        flash("Email cannot be empty")
        errors = True
    if not EMAIL_REGEX.match(content['email']):
        flash("Invalid Email Address!")
        errors = True
    if len(content['birthdate']) < 1:
        flash("Birthdate cannot be empty")
        errors = True
    if len(content['password']) < 1:
        flash("Password cannot be empty")
        errors = True
    if len(content['password']) > 8:
        flash("You can't remember a password that long")
        errors = True
    if len(content['confirmpassword']) < 1:
        flash("You must type in a password confirmation!")
        errors = True
    if content['password'] != content['confirmpassword']:
        flash("Passwords don't match")
        errors = True
    if errors:
        return redirect("/")
    else:
        return render_template('show.html',content=content)

app.run(debug=True)      # Run the app in debug mode.
