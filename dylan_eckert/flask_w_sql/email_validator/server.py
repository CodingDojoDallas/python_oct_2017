from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'emaildb')
app.secret_key = "key"
# an example of running a query

@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails)

@app.route('/newemail', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    data = { 'email': request.form['email'].lower() }

    query = "SELECT * FROM emails WHERE email=:email"
    emails = mysql.query_db(query, data)

    if len(emails) == 0:
        query = "INSERT INTO emails (email) VALUES (:email)"
        mysql.query_db(query, data)
        return redirect('/success')
    else:
        flash("That email already exists!")
        return redirect('/')



@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

app.run(debug=True)
