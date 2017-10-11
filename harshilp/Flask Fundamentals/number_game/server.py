from random import randrange
from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = 'SecreT'
@app.route('/')
def landing():
    if 'state' not in session:
        session['state'] = 'start'
    if 'ans' not in session:
        session['ans'] = randrange(0,101)
    print session['ans']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print request.form['guess']
    if int(request.form["guess"]) < session['ans']:
        session['state'] = 'low'
    elif int(request.form["guess"]) > session['ans']:
        session['state'] = 'high'
    else:
        session['state'] = 'end'
    print session['state']
    return redirect('/')

@app.route('/again', methods=["POST"])
def again():
    session.pop('ans')
    session.pop('state')
    return redirect('/')
app.run(debug=True)