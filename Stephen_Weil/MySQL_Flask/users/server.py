from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT id, name, email, date_format(friend_since, '%M ' '%D, ' '%Y') as joined FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/create', methods=['post'])
def add_user():
    query = "INSERT INTO friends (name, email, friend_since) VALUES (:name, :email, NOW())"
    name = request.form['first'] + " " + request.form['last']
    data = {
        'name': name,
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/<id>')
def show_user(id):
    query = "SELECT id, name, email, date_format(friend_since, '%M ' '%D, ' '%Y') as joined FROM friends WHERE id = :id LIMIT 1"
    data = {'id': id}
    user = mysql.query_db(query, data)
    return render_template('user.html', user=user[0])

@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/edit/<idnum>')
def edit_page(idnum):
    query = "SELECT id, name, email, date_format(friend_since, '%M ' '%D, ' '%Y') as joined FROM friends WHERE id = :id LIMIT 1"
    data = {'id': idnum}
    user = mysql.query_db(query, data)
    name = user[0]['name'].split()
    first_name = name[0]
    last_name = name[1]
    return render_template('edit.html', user=user[0], first=first_name, last=last_name)

@app.route('/update/<idnum>', methods=['post'])
def update_user(idnum):
    query = "UPDATE friends SET name = :name, email = :email WHERE id = :id;"
    name = request.form['first'] + " " + request.form['last']
    data = {
        'id': idnum,
        'name': name,
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<idnum>')
def delete_user(idnum):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': idnum}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)