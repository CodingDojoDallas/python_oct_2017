from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_users=user) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, friend_since, created_at, updated_at) VALUES (:name, :age, NOW(), NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend=friends[0])

app.run(debug=True)