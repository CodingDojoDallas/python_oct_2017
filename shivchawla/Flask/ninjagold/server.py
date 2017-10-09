import random
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__) #generating an instance of the flask class
app.secret_key = "secretkey" #encrypts and decrypts cookies

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'info' not in session:
        session['info'] = []
    print session['gold']
    return render_template('ninja_gold.html')

@app.route('/process_money', methods=['post'])
def dolladollabill():
    if request.form['building'] == 'farm':
        diff = random.randint(10, 20)
        session['gold'] += diff
        session['info'].append("You just gained {} gold!".format(diff))
    elif request.form['building'] == 'cave':
        diff = random.randint(5, 10)
        session['gold'] += diff
        session['info'].append("You just gained {} gold!".format(diff))
    elif request.form['building'] == 'house':
        diff = random.randint(2, 5)
        session['gold'] += diff
        session['info'].append("You just gained {} gold!".format(diff))
    elif request.form['building'] == 'casino':
        diff = random.randint(-50, 50)
        session['gold'] += diff
        session['info'].append("You dirty gambler! {} gold!".format(diff))
    return render_template('ninja_gold.html')

@app.route('/reset')
def reset():
    session['gold'] = 0
    session['info'] = []
    return render_template('ninja_gold.html')

app.run(debug=True) # run our server