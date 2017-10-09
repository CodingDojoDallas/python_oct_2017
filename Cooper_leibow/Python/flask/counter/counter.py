from flask import Flask, render_template, redirect, session 
app = Flask(__name__)
app.secret_key = "StupidSecret"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
     
    session['counter'] += 1

    return render_template('home.html')

@app.route('/reset')
def reset():
    session ['counter'] = 0
    return redirect('/')

@app.route('/addtwo')
def addTwo():
    session ['counter'] += 1 
    return redirect ('/')

app.run(debug=True)


