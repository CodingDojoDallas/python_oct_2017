from flask import Flask, redirect, render_template, session, flash, request
from mysqlconnection import MySQLConnector
import md5
import re
import os, binascii
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'login_register')
app.secret_key = 'Boo'

def validation():
    error = False
    if len(request.form['first_name']) < 1:
        flash('First name cannot be blank', 'Error:FirstName')
        error = True
    elif request.form['first_name'].isalpha() == False:
        flash('First name must contain only letters', 'Error:FirstName')
        error = True

    if len(request.form['last_name']) < 1:
        flash('Last name cannot be blank', 'Error:LastName')
        error = True
    elif request.form['last_name'].isalpha() == False:
        flash('Last name must contain only letters', 'Error:LastName')
        error = True

    if len(request.form['email']) < 1:
        flash('Email cannot be blank', 'Error:Email')
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address', 'Error:Email')
        error = True

    if len(request.form['password']) < 1:
        flash('Password cannot be blank', 'Error:Password')
        error = True
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 7 characters', 'Error:Password')
        error = True
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Password must contain at least one lowercase, uppercase and digit', 'Error:Password')
        error = True

    if len(request.form['cpassword']) < 1:
        flash('Password confirmation cannot be blank', 'Error:PasswordConfirmation')
        error = True
    elif request.form['password'] != request.form['cpassword']:
        flash('Passwords don\'t match', 'Error:PasswordConfirmation')
        error = True

    return error != True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if validation() == False:
        return redirect('/')
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        salt =  binascii.b2a_hex(os.urandom(15))
        password = request.form['password']
        hashed_pw = md5.new(password + salt).hexdigest()
        query = 'INSERT INTO users(first_name, last_name, email, salt, password, created_at, updated_at) VALUES(:first_name, :last_name, :email,:salt, :password, NOW(), NOW())'
        data = {'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'salt': salt,
                'password': hashed_pw
        }
        mysql.query_db(query,data)
        return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    query = 'SELECT salt, password FROM users where email = :email'
    data = {'email':email}
    valid = mysql.query_db(query,data)

    if len(valid) < 1:
        flash('Not a valid log in ID', 'Error:LoginFirstName')
        return redirect('/')
    else:
        if md5.new(password + valid[0]['salt']).hexdigest() == valid[0]['password']:
            return render_template('success.html')
        else:
            flash('Password invalid', 'Error:LoginPassword')
            return redirect('/')

app.run(debug=True)