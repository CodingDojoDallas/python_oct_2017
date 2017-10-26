from flask import Flask, render_template, session, redirect, flash, request
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "stupid"

@app.route('/')
def home():
    if 'email' not in session:
        session['email'] = ""    
    email = session['email']
    if 'fist_name' not in session:
        session['first_name'] = ""
    first_name = session['first_name']
    if 'last_name' not in session:
        session['last_name'] = ""
    last_name = session['last_name']
    if 'password' not in session:
        session['password'] = ""    
    password = session['password']
    if 'confirm' not in session:
        session['confirm'] = ""    
    confirm = session['confirm']
    return render_template('index.html')

@app.route('/submit', methods=['POST'] )
def submit():
    data = {
        "email": request.form['email'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "password": request.form['password'],
        "confirm": request.form['confirm'],
    }
    session['email'] = data['email']
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    session['password'] = data['password']
    session['confirm'] = data['confirm']
    print session['email']
    if len(request.form['email']) > 0: 
        flash("Success! Your email works")
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Email must have only characters")
        else: 
            flash("Success! Your email works")
    else: 
        flash("Need name")
    if len(request.form['first_name']) > 0: 
        flash("Success! Your first name is good")
        if request.form['first_name'].isalpha() == True:
            flash("Success")
        else: 
            flash("First name must contain only characters")
    else: 
        flash("need first name!")
    if len(request.form['last_name']) > 0: 
        flash("Success! Your last name is good")
    else: 
        flash("need last name!")
    if len(request.form['password']) > 1: 
        flash("Success! Your password works")
        if len(request.form['password']):
            flash("Success! Your password was justttttt right")
        else: 
            flash("Your password must be less than 8 characters")
    else: 
        flash("need password!")
    if len(request.form['confirm']) > 1: 
        flash("Success! You know how to make a password")
    else: 
        flash("need confirm password!")
    if request.form['password'] == request.form['confirm']:
        flash("Success! Passwords match")
    else: 
        flash("Passwords must match")
    return redirect('/')
app.run(debug=True)