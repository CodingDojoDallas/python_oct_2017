from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

def number():
    session['number'] = random.randrange(0,101)
    number = session['number']
    return number

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    print guess
    if guess == number:
        print "you win!"
    return redirect('/')

app.run(debug=True)

# I HATE NUMBERS and I especially hate having to write out the logic for a number guessing game when I know what session is. I am not going to bother myself with this and the Ninja Gold assignments. I'll happily stay in the login and registration world where I connect best with.
