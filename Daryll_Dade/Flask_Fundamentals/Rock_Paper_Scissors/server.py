from flask import Flask, render_template, redirect, request, session
from random import randint
app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def index():
    if 'info' not in session:
        session['info'] = ' '
    if 'wincount' not in session:
        session['wincount'] = 0
    if 'tiecount' not in session:
        session['tiecount'] = 0
    if 'losscount' not in session:
        session['losscount'] = 0
    return render_template('index.html')


@app.route('/process_play', methods=['POST'])
def process_play():
    userchoice = request.form['Button']
    computerchoice = randint(0, 2)
    list = ["Rock", "Paper", "Scissors"]
    computerchoice = list[computerchoice]
    if userchoice == "Rock" and computerchoice == "Rock":
        result = "tie"
    elif userchoice == "Rock" and computerchoice == "Paper":
        result = "LOSE"
    elif userchoice == "Rock" and computerchoice == "Scissors":
        result = "win"
    elif userchoice == "Paper" and computerchoice == "Rock":
        result = "win"
    elif userchoice == "Paper" and computerchoice == "Paper":
        result = "tie"
    elif userchoice == "Paper" and computerchoice == "Scissors":
        result = "LOSE"
    elif userchoice == "Scissors" and computerchoice == "Rock":
        result = "LOSE"
    elif userchoice == "Scissors" and computerchoice == "Paper":
        result = "win"
    elif userchoice == "Scissors" and computerchoice == "Scissors":
        result = "tie"
    info = "The computer picked " + computerchoice + \
        " and you picked " + userchoice + "." + "  You " + result + "."

    session['info'] = info
    if result == "win":
        session['wincount'] += 1
    if result == "tie":
        session['tiecount'] += 1
    if result == "LOSE":
        session['losscount'] += 1
    return redirect('/')


app.run(debug=True)
