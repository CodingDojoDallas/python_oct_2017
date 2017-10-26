from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT id, name, age, date_format(friend_since, '%M') as mon, year(friend_since) as year FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/add', methods=['post'])
def add_friend():
    query = "INSERT INTO friends (name, age, friend_since) VALUES (:name, :age, NOW())"
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)