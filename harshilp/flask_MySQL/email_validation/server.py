from flask import Flask, render_template, redirect, request, flash, session
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'emails')
app.secret_key = 'kittens'

@app.route('/')
def index():
    if 'email' not in session:
        session['email'] = ''
    return render_template('index.html')

@app.route('/enter', methods=['POST'])
def enter():
    session['email'] = request.form['email']
    valid = True
    if len(session['email']) < 1:
        flash('No email address entered')
        valid = False
    elif not EMAIL_REGEX.match(session['email']):
        flash('Invalid email address')
        valid = False
    if valid:
        query = 'Select address from emails'
        emails = mysql.query_db(query)
        for email in emails:
            if email['address'] == session['email']:
                flash('Email already in database')
                return redirect('/')
        print 'asdf'
        query = 'INSERT INTO emails(address, created_at, updated_at) VALUES(:email, NOW(), NOW())'
        data = {'email':session['email']
        }
        mysql.query_db(query, data)
        query = 'Select address, date_format(created_at, "%d/%m/%Y %r") as time from emails'
        emails = mysql.query_db(query)
        return render_template('success.html', emails = emails)
    else:
        return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    query = 'DELETE FROM emails WHERE id > 0'
    mysql.query_db(query)
    session.clear()
    return redirect('/')

@app.route('/return', methods=['POST'])
def returnHome():
    return redirect('/')

app.run(debug=True)
