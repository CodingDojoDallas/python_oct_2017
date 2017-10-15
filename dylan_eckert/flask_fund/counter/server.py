from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

@app.route('/')
def index():
    route = '/'
    if route == '/':
        session['count'] += 1
    return render_template("index.html")

app.run(debug=True)
