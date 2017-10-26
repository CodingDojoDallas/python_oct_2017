
import md5, os, binascii, random
from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "stupid"
mysql = MySQLConnector(app,'login_reg')


@app.route('/')
def index():
    return render_template('index.html')
    if id not in session:
        session['id'] = id

@app.route('/register', methods = ['POST'])
def register():
    valid = True
    newData = {
        'email': request.form['email'],
        'password': request.form['password'],
        'cPassword': request.form['cPassword'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    email = request.form['email']
    password = request.form['password']
    cPassword = request.form['cPassword']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    if first_name < 2:
        flash("First name must be greater than 2 characters")
        valid = False
    elif not first_name.isalpha():
        flash("First name must contain only letters")
        valid = False        

    if last_name < 2:
        flash("Last name must be greater than 2 characters")
        valid = False
    elif not last_name.isalpha():
        flash("Last name must contain only letters")
        valid = False
    
    if len(email) < 1 or len(password) < 1 or len(cPassword) < 1 :
        flash("Email and password required")
        valid = False
    elif len(password) < 8:
        flash("Password too short")
        valid = False
    elif password != cPassword:
        flash("Passwords dont match")
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash("Not a valid email")
        valid = False

    if valid:    
        query = "SELECT email FROM users WHERE email = :email"
        emails = mysql.query_db(query, {'email':email})
        if emails:
            flash("You dumb piece of shit. Emails cannot match.")
        else:
            newData['salt'] = binascii.b2a_hex(os.urandom(15))
            newData['hash'] = md5.new(request.form['password']+newData['salt']).hexdigest()
            query = "INSERT INTO users (first_name, last_name, email, password, salt, hash, created_at, updated_at) Values ( :first_name, :last_name, :email, :password, :salt, :hash,  NOW(), NOW() )" 
            session['user_id'] = mysql.query_db(query, newData)
            print session['user_id']
            print "You registered!"
            return redirect('/success')

    return redirect('/')
@app.route('/login', methods = ['POST'])
def login():
    valid = True
    userData = {
        'user_email': request.form['user_email'],
        'user_password': request.form['user_password'],
    }
    if request.form['user_email'] < 2 :
        valid = False
        flash("You fail")
    elif request.form['user_password'] < 2:
        valid = False
        flash("Wrong")
    if valid:
        query = "SELECT * FROM users WHERE email = :email"
        users = mysql.query_db(query, {'email':userData['user_email']})
        if len(users) > 0:
            user = users[0]
            if md5.new(request.form['user_password']+user['salt']).hexdigest() == user['hash']:
            # password check
                flash("You are logged in")
                session['user_id'] = user['id']
                return redirect('/success')
            else:
                flash("Login failed")
                return redirect ('/')
        else:
            flash("User not found")
            return redirect ('/')

@app.route('/success')
def show():
    query = "SELECT * from users WHERE id = :id"
    data = {'id' :session['user_id']}
    users = mysql.query_db(query, data)
    print data
    return render_template('show.html', user = users[0])


# @app.route('/submit', methods = ['POST'])
# def submit():
#     print type(request.form['email_address'])
#     if not EMAIL_REGEX.match(request.form['email_address']):
#         flash("Not a valid email")
#     else: 
#         flash("Success")
#         query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email_address, now(), now())"
#         formData = { #insert data as a dictionary
#         'email_address': request.form['email_address']
#         }
#         mysql.query_db(query, formData) 
#     return redirect ('/')

app.run(debug=True)

