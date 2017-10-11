from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "somesecretkey"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = request.form['guess']
    if int(user_guess) > session['number']:
        ret = render_template('index.html', message="Too High!", color="red")
    elif int(user_guess) < session['number']:
        ret = render_template('index.html', message="Too Low!", color="red")
    elif int(user_guess) == session['number']:
        message = "Got it! " + user_guess + " was the number!"
        ret = render_template('index.html', message=message, color="green", reset="yes")
    return ret

@app.route('/reset')
def reset():
    session.pop('number')
    return redirect('/')

app.run(debug=True)