from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector 
import random
import sys



ROCK = 0
PAPER = 1
SCISSORS = 2



def log(obj):
	print(obj, file=sys.stderr)


app = Flask(__name__)            

app.secret_key = "secret"

mysql = MySQLConnector(app, 'mydb') 



@app.route("/")
def index():
	log(mysql.query_db("SELECT * FROM user"))
	return render_template("index.html")

	
	
@app.route("/game")
def game():
	query = "SELECT wins, losses, ties FROM user WHERE name = :name"
	data = mysql.query_db(query, {'name': session['name']})
	
	return render_template("game.html", name = session['name'], wins = data[0]['wins'], losses = data[0]['losses'], ties = data[0]['ties'])
	
	
	
@app.route("/login", methods=["POST"])
def login():
	if not 'name' in session:
		if not 'name' in request.form:
			redirect ('/')
		session['name'] = request.form['name']
	
	session['name'] = request.form['name']
	

	temp = mysql.query_db("SELECT COUNT(name) AS count FROM user WHERE name = :name", {"name":session['name']})
	if temp[0]['count'] == 0:
		mysql.query_db("INSERT INTO user(name, wins, losses, ties) VALUES( :name, 0,0,0 )", {"name": session['name']})
		log(mysql.query_db("SELECT * FROM user"))
	
	return redirect("/game")
	
	
@app.route('/process', methods=['POST'])
def process():
	computer = random.randint(0,2)
	result = ""
	
	if computer == ROCK:
		if int(request.form['choice']) == PAPER:
			flash("The Computer picked rock \n you picked paper, You Win!")
			result = "win"
			
		elif int(request.form['choice']) == SCISSORS:
			flash("The Computer picked rock \n you picked scissors, You Lose!")
			result = "lose"
		elif int(request.form['choice']) == ROCK:
			flash("The Computer picked rock \n you picked rock, You tie!")
			result = "tie"
	elif computer == PAPER:
		if int(request.form['choice']) == PAPER:
			flash("The Computer picked paper \n you picked paper, You Tie!")
			result = "tie"
		elif int(request.form['choice']) == SCISSORS:
			flash("The Computer picked paper \n you picked scissors, You Win!")
			result = "win"
		elif int(request.form['choice']) == ROCK:
			flash("The Computer picked paper \n you picked rock, You Lose!")
			result = "lose"
	elif computer == SCISSORS:
		if int(request.form['choice']) == PAPER:
			flash("The Computer picked scissors \n you picked paper, You Lose!")
			result = "lose"
		elif int(request.form['choice']) == SCISSORS:
			flash("The Computer picked scissors \n you picked scissors, You Tie!")
			result = "tie"
		elif int(request.form['choice']) == ROCK:
			flash("The Computer picked scissors \n you picked rock, You Win!")
			result = "win"
	
	if result == "win":
		query= "UPDATE user SET wins = wins+1 WHERE name = :name"
		data = {'name': session['name']}
		mysql.query_db(query, data)
	if result == "lose":
		query= "UPDATE user SET losses = losses+1 WHERE name = :name"
		data = {'name': session['name']}
		mysql.query_db(query, data)
	if result == "tie":
		query= "UPDATE user SET ties = ties+1 WHERE name = :name"
		data = {'name': session['name']}
		mysql.query_db(query, data)
	
		
	return redirect('/game')
	
	


app.run(debug=True) 
