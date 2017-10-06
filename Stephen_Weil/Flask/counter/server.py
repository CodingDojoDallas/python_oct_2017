from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 's0m3s3cr3tk3y'

@app.route('/')
def counter():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/plustwo', methods=['POST'])
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)