from flask import flash, Flask, render_template, request, redirect   # Import Flask and the class of render_template, request and redirect
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
    content = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    if len(content["name"]) < 1:
        flash("Name cannot be empty")
        print "empty"
        return redirect('/')
    if len(content["comment"]) < 1:
        flash("Comments can't be empty")
        return redirect('/')
    elif len(content["comment"]) > 120:
        flash("Comments too many characters")
        return redirect('/')
    return render_template('show.html',content=content)

app.run(debug=True)      # Run the app in debug mode.

''' app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    return redirect('/') '''