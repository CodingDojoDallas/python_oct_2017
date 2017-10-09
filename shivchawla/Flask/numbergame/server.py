import random
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__) #generating an instance of the flask class
app.secret_key = "secretkey" #encrypts and decrypts cookies

@app.route('/')
def store():
    session['guess'] = random.randint(0, 101)
    return render_template('game.html')

@app.route('/')
def store():
    session['guess'] = random.randint(0, 101)
    return render_template('game.html')

@app.route('/guess', methods=['post'])
def guess():
    userguess= int(request.form['guess'])
    if int(session['guess']) == int(userguess):
        return render_template('playgame.html',userguess=userguess)
    else:
        return render_template('playgame.html',userguess=userguess)

app.run(debug=True) # run our server