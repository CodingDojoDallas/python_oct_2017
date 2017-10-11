from flask import Flask, render_template, request, session, flash, redirect
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = 'SecreT'

def validation():
    error = False
    if len(request.form['first_name']) < 1:
        flash('First name cannot be blank', 'Error:FirstName')
        error = True
    elif request.form['first_name'].isalpha() == False:
        flash('First name must contain only letters', 'Error:FirstName')
        error = True
    else:
        session['firstname'] = request.form['first_name']

    if len(request.form['last_name']) < 1:
        flash('Last name cannot be blank', 'Error:LastName')
        error = True
    elif request.form['last_name'].isalpha() == False:
        flash('Last name must contain only letters', 'Error:LastName')
        error = True
    else:
        session['lastname'] = request.form['last_name']

    if len(request.form['email']) < 1:
        flash('Email cannot be blank', 'Error:Email')
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address', 'Error:Email')
        error = True
    else:
        session['email'] = request.form['email']

    if len(request.form['password']) < 1:
        flash('Password cannot be blank', 'Error:Password')
        error = True
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 7 characters', 'Error:Password')
        error = True
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Password must contain at least one lowercase, uppercase and digit', 'Error:Password')
        error = True
    else:
        session['password'] = request.form['password']

    if len(request.form['confirm']) < 1:
        flash('Password confirmation cannot be blank', 'Error:PasswordConfirmation')
        error = True
    elif request.form['password'] != request.form['confirm']:
        flash('Passwords don\'t match', 'Error:PasswordConfirmation')
        error = True
    else:
        session['confirm'] = request.form['confirm']

    if len(request.form['birthdate']) < 1:
        flash('Birthdate cannot be blank', 'Error:Birthdate')
        error = True
    else:
        session['birthdate'] = request.form['birthdate']
        today = datetime.now()
        bday = datetime.strptime(session['birthdate'], "%Y-%m-%d")

        if today < bday:
            flash('Please pick a valid birthdate in the past', 'Error:Birthdate')
            error = True

    return error != True

@app.route('/')
def index():
    if 'firstname' not in session:
        session['firstName'] = ''
    if 'lastname' not in session:
        session['lastName'] = ''
    if 'birthdate' not in session:
        session['birthdate'] = ''
    if 'email' not in session:
        session['email'] = ''
    if 'password' not in session:
        session['password'] = ''
    if 'confirm' not in session:
        session['confirm'] = ''

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if validation() == False:
        return redirect('/')
    else:
        flash('You\'ve been successfully registered! :)', 'Success')
        return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
