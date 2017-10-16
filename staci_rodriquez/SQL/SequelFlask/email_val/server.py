from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email_val')
# an example of running a query

@app.route('/')
def index():                         # run query with query_db()
    return render_template('index.html')

@app.route('/success')
def success():                         # run query with query_db()
    return render_template('success.html')

@app.route('/email', methods=['post'])
def email():
    
    valid = True

    email = request.form['email']
    print "/email"
    # if len(email) < 1:
    #     flash('Email is not valid!')

    # if valid:
    #     query = "SELECT user_id FROM users WHERE email = :email"
    #     data = {'email': email}
    #     users = db.query_db(query, data)
    #     print users

        # if len(users) > 0:



    return redirect('/')
    return redirect('/success')

    

    


app.run(debug=True)
