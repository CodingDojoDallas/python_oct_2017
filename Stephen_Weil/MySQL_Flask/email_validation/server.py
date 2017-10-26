from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "nasbu76q2123mf"
mysql = MySQLConnector(app, 'emaildb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/submit', methods=['post'])
def submit():
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash("Not a valid email address!")
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, added_at) VALUES (:email, NOW())"
        data = {'email': email}
        mysql.query_db(query, data)
        flash_message = "The email address you entered (" + email + ") is valid. Thank you!"
        flash(flash_message)
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT id, email, DATE_FORMAT(added_at, '%m' '/' '%d' '/' '%Y' ' ' '%l' ':' '%i' ' ' '%p') as add_time FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', emails=emails)

@app.route('/delete', methods=['post'])
def delete():
    id_to_del = request.form['whichid']
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': id_to_del}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)