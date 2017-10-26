
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector



app = Flask(__name__)
mysql = MySQLConnector(app,'email_val')
app.secret_key = 'some_secret'

@app.route('/')
def index():
    query  = "SELECT * FROM users"
    users = mysql.query_db(query)
    print users

    return render_template('index.html')

@app.route('/success', methods=['POST'])
def check():
    email = request.form['email']

    query  = "SELECT * FROM users WHERE users.email = :email"

#query will look for the emial in users where it is equal to email
    data = {'email':email}

    results = mysql.query_db(query, data) # Need to pass data as second arguement (mysqlconnection.py line#25)
    if len(results) > 0:
        flash("email taken, exist")
        return redirect('/')
    elif len(results) == 0:
        flash("The email address you entered " + email + " is a VALID email address! Thank you!")

        # insert the new email to the db
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW() )"
        data = {'email': request.form['email']}
        print email
        mysql.query_db(query,data) # Need to pass data as second arguement (mysqlconnection.py line#25)

        # select query for all the emails
        query = "SELECT * FROM users ORDER BY id DESC"
        users = mysql.query_db(query)

        return render_template('success.html', users = users)



app.run(debug=True)
