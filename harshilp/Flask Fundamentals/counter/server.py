from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def landing():
    if 'count' in session:
        session['count'] +=1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/plusTwo', methods=['POST'])
def plusTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)