from flask import Flask, request, redirect, render_template, session, flash
import re, md5, os, binascii
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'login_register')
app.secret_key = "key"

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/register', methods=['POST'])
def register():
    valid = True

    data = {
    'salt': binascii.b2a_hex(os.urandom(15)),
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'].lower(),
    'password': request.form['password'],
    'pass_conf': request.form['pass_conf'],
    }

    #LOGIC FOR FIRST NAME:
    if len(data['first_name']) < 2:
        flash("Please enter a valid first name")
    elif not data['first_name'].isalpha():
        flash("Please us characters a-z")

    #LOGIC FOR LAST NAME:
    if len(data['last_name']) < 2:
        flash("Please enter a valid last name")
    elif not data['first_name'].isalpha():
        flash("Please us characters a-z")

    #LOGIC FOR PASSWORD and PASS CONF:
    if len(data['password']) < 8:
        flash("Password must be at least 8 characters long")
    elif data['password'] != data['pass_conf']:
        flash("Passwords don't match")
    #LOGIC FOR EMAIL:
    if len(data['email']) < 1:
        flash("Please enter an email")
    elif not EMAIL_REGEX.match(data['email']):
        flash("Please enter a valid email")

    if valid:
        data['password'] = md5.new(data['password']+data['salt']).hexdigest()
        query = "SELECT * FROM users WHERE email=:email"
        emails = mysql.query_db(query, data)

        if len(emails) == 0:
            query = "INSERT INTO users (first_name, last_name, password, email, salt) VALUES (:first_name, :last_name, :password, :email, :salt)"
            mysql.query_db(query, data)
            return redirect('/')
        else:
            flash("That email already exists!")

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    login = {
    'email': request.form['email'].lower(),
    'password': request.form['password']
    }
    query = "SELECT * FROM users WHERE email=:email"
    users = mysql.query_db(query, login)


    if md5.new(login['password']+users[0]['salt']).hexdigest() == users[0]['password']:
        flash("Login Successful!")
        return redirect('/')
    else:
        flash("Please enter an email and password")
        return redirect('/')

app.run(debug=True)
