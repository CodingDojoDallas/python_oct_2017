from flask import Flask, request, redirect, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    valid = True

    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'].lower(),
    'password': request.form['password'],
    'pass_conf': request.form['pass_conf'],
    }

    #LOGIC FOR FIRST NAME:
    if len(data['first_name']) < 2:
        flash("Please enter a valid first name")
        valid = False
    elif not data['first_name'].isalpha():
        flash("Please us characters a-z")
        valid = False

    #LOGIC FOR LAST NAME:
    if len(data['last_name']) < 2:
        flash("Please enter a valid last name")
        valid = False
    elif not data['first_name'].isalpha():
        flash("Please us characters a-z")
        valid = False

    #LOGIC FOR PASSWORD and PASS CONF:
    if len(data['password']) < 9:
        flash("Password must be at least 9 characters long")
        valid = False
    elif data['password'] != data['pass_conf']:
        flash("Passwords don't match")
        valid = False
    #LOGIC FOR EMAIL:
    if len(data['email']) < 1:
        flash("Please enter an email")
        valid = False
    elif not EMAIL_REGEX.match(data['email']):
        flash("Please enter a valid email")
        valid = False

    if valid:
        flash("Thank you for submitting your info")

    return redirect('/')

app.run(debug=True)
