from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
@app.route('/')
def index():
    query = 'SELECT name, age, date_format(created_at, \'%M %D\') as since, Year(created_at) as year FROM friends Order by created_at DESC'
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/add', methods=['POST'])
def add():
    query = 'INSERT INTO friends(name, age, created_at, updated_at) VALUES(:name, :age, NOW(), NOW());'
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)