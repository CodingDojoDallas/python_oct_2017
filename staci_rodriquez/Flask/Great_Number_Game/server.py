from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'newenglandclamchowder'

@app.route('/')
def randomize():
    if 'randnum' not in session:
        session['randnum'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['randnum']:
        return render_template('index.html', message=request.form['guess']+" was the number!", color="green", replay="True")
    elif int(request.form['guess']) > session['randnum']:
        return render_template('index.html', message=request.form['guess']+" was Too High!", color="red")
    else:
        return render_template('index.html', message=request.form['guess']+" was Too Low!", color="red")

@app.route('/reset')
def reset():
    session.pop('randnum')

    return redirect('/')

app.run(debug=True)
