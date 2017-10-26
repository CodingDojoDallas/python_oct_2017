from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "wtfff"

@app.route('/')
def home():
    if 'your_gold' not in session:
        session['your_gold'] = 0
    your_gold = session['your_gold']
    if 'info' not in session:
        session['info'] = []
    info = session['info']
    print your_gold
    return render_template('ninja_gold.html', your_gold = your_gold, info = info)

@app.route('/process_money', methods=['POST'])
def process_money():
    import random
    print random.randint(0,21)
    if request.form['building'] == "farm":
        print "working"
        f = random.randint(0,21)
        session['your_gold'] += f
        session['info'].append("You earned " + str(f) + " gold. Nice!")
        print session['info']
    elif request.form['building'] == "cave":
        c = random.randint(5,11)
        session['your_gold'] += c
        session['info'].append("You earned " + str(c) + " gold. Way to go!")
    elif request.form['building'] == "house":
        h = random.randint(2,6)
        session['your_gold'] += h
        session['info'].append("You earned " + str(h) + " gold. Not bad")
    elif request.form['building'] == "casino":
        cas = random.randint(-50,51)
        session['your_gold'] += cas
        if cas < 0: 
            session['info'].append("You lost " + str(cas) + " gold. Loser")
        else:
             session['info'].append("You won " + str(cas) + " gold. Cheater!!")
    session.modified = True
    return redirect('/')

@app.route('/reset')
def reset():
    session['your_gold'] = 0
    session['info'] = []
    return redirect('/')

app.run(debug=True)