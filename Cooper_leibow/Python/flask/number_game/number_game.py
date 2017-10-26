from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Shhhhhh"


@app.route('/')
def home():
    import random 
    if 'person_num' not in session:
        session['person_num'] = 0
    person_num = session['person_num']
    print person_num
    if 'stored_num' not in session:
        session['stored_num'] = random.randint(1,101)
    stored_num = session['stored_num']
    return render_template('number_game.html', person_num = person_num, stored_num = stored_num)

@app.route('/submit', methods=['POST'])
def submit():
    session['person_num'] = request.form['person_num'] 
    return redirect('/')

@app.route('/reset')
def reset():
    for key,value in session.items():
        del session[key]

app.run(debug=True)