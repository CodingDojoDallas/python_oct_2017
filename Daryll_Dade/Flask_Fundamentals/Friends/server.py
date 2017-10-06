from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = Mysqlconnectior(app, 'friends')

@app.route('/')
def index():
    print "mysqlconnector"
    return render_template("index.html")

app.run(debug=True)
