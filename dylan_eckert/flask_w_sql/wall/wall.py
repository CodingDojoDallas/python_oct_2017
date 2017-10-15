from flask import Flask, request, redirect, render_template, session, flash
import re, md5, os, binascii
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
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
    'username': request.form['username'],
    'password': request.form['password'],
    'pass_conf': request.form['pass_conf'],
    }

    #LOGIC FOR USERNAME:
    if len(data['username']) < 2:
        flash("Please enter a valid username")
    elif not data['username'].isalpha():
        flash("Please use characters a-z")

    #LOGIC FOR PASSWORD and PASS CONF:
    if len(data['password']) < 8:
        flash("Password must be at least 8 characters long")
    elif data['password'] != data['pass_conf']:
        flash("Passwords don't match")

    if valid:
        data['password'] = md5.new(data['password']+data['salt']).hexdigest()
        query = "SELECT * FROM users WHERE username=:username"
        users = mysql.query_db(query, data)

        if len(users) == 0:
            query = "INSERT INTO users (password, username, salt) VALUES (:password, :username, :salt)"
            mysql.query_db(query, data)
            return redirect('/')
        else:
            flash("That username already exists!")

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    login = {
    'username': request.form['username'].lower(),
    'password': request.form['password']
    }
    query = "SELECT * FROM users WHERE username=:username"
    users = mysql.query_db(query, login)


    if md5.new(login['password']+users[0]['salt']).hexdigest() == users[0]['password']:
        flash("Login Successful!")
        return redirect('/')
    else:
        flash("Please enter your username and password")
        return redirect('/wall')

app.run(debug=True)
