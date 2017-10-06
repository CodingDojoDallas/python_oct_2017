from flask import Flask, render_template, redirect, request, session
from random import randrange
import datetime
app = Flask(__name__)
app.secret_key = 'SecreT'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['log'] = []
        session['debt'] = 'no'
        session['len'] = 0

    session['len'] = len(session['log'])
    
    if int(session['gold']) < 0:
        session['debt'] = 'yes'
    elif int(session['gold']) > 100:
        session['debt'] = 'nah'
    else:
        session['debt'] = 'no'
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    time = datetime.datetime.now()
    if request.form['building'] == 'farm':
        val = randrange(10,21)
        session['log'].append('Earned {} gold from the {}! {}'.format(val, request.form['building'], time))
        session['gold'] += val
    elif request.form['building'] == 'cave':
        val = randrange(5,11)
        session['log'].append('Earned {} gold from the {}! {}'.format(val, request.form['building'], time))
        session['gold'] += val
    elif request.form['building'] == 'house':
        val = randrange(2,6)
        session['log'].append('Earned {} gold from the {}! {}'.format(val, request.form['building'], time))
        session['gold'] += val
    elif request.form['building'] == 'casino':
        luck = randrange(0,5)
        val = randrange(0,51)
        if luck != 2: 
            session['log'].append('Lost {} gold from the {}! {}'.format(val, request.form['building'], time))
            session['gold'] -= val
        else:
            session['log'].append('Earned {} gold from the {}! {}'.format(val, request.form['building'], time))            
            session['gold'] += val
    return redirect('/')
app.run(debug=True)