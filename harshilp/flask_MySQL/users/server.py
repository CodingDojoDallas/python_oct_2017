from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'users')
app.secret_key = 'secret'

@app.route('/users')
def users():
    query = 'SELECT id, date_format(created_at, "%M %D, %Y") as date, CONCAT(first_name, " ", last_name) as name, email FROM users'
    users = mysql.query_db(query)
    return render_template('users.html', users = users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
    name = '{} {}'.format(request.form['first_name'], request.form['last_name'])
    email = request.form['email']
    query = 'INSERT INTO users(first_name,last_name, email, created_at, updated_at) VALUES(:first_name,:last_name, :email, NOW(), NOW())'
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':email
    }
    mysql.query_db(query,data)
    return redirect('/users')

@app.route('/users/<user_id>')
def show(user_id):
    query = 'SELECT id, date_format(created_at, "%M %D, %Y") as date, CONCAT(first_name, " ", last_name) as name, email FROM users WHERE users.id = :user_id'
    data = {
        'user_id':user_id
    }
    user = mysql.query_db(query, data)
    return render_template('show.html', user = user[0])

@app.route('/users/<user_id>/edit')
def edit(user_id):
    return render_template('edit.html', user_id = user_id)

@app.route('/users/<user_id>', methods=['POST'])
def update(user_id):
    query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() where users.id = :user_id'
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'user_id':user_id
    }
    mysql.query_db(query, data)
    return redirect('/users/'+user_id)

@app.route('/users/<user_id>/delete', methods=['GET'])
def delete(user_id):
    query = 'DELETE FROM users WHERE users.id = :user_id'
    data = {
        'user_id':user_id
    }
    mysql.query_db(query, data)
    return redirect('/users')

app.run(debug=True)
