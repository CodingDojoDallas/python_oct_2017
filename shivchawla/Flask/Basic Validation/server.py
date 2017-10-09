from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
    else:
        ("Success! Your name is {}".format(request.form['name']))
    return redirect('/')
app.run(debug=True)

#If you wanted to validate an email address
''' app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    return redirect('/') '''