from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "adiyfc9n9382"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    building = request.form['building']
    if building == "farm":
        gold_won = random.randint(10,20)
        activity = "Earned " + str(gold_won) + " gold from the farm! (" + str(datetime.now()) + ")"
    elif building == "cave":
        gold_won = random.randint(5,10)
        activity = "Earned " + str(gold_won) + " gold from the cave! (" + str(datetime.now()) + ")"
    elif building == "house":
        gold_won = random.randint(2,5)
        activity = "Earned " + str(gold_won) + " gold from the house! (" + str(datetime.now()) + ")"
    elif building == "casino":
        if random.random() >= .5:
            gold_won = random.randint(0,50)
            activity = "Won " + str(gold_won) + " gold from the casino! (" + str(datetime.now()) + ")"
        else:
            gold_won = random.randint(0,50)*(-1)
            activity = "Lost " + str(gold_won*-1) + " gold at the casino! Ouch! (" + str(datetime.now()) + ")"
    if 'gold' not in session:
        session['gold'] = gold_won
    else:
        session['gold'] += gold_won
    if 'activities' not in session:
        session['activities'] = [activity]
    else:
        session['activities'].append(activity)
    return redirect('/')

app.run(debug=True)