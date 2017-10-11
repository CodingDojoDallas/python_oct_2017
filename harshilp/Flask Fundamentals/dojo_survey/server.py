from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'SecreT'

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash('Name field cannot be blank!')
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash('Please enter a comment!')
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash('Comment too long. Less than 120 characters pliz...')
        return redirect('/')
    name = request.form['name']
    loc = request.form['dojo_location']
    lang = request.form['favorite_language']
    comment = request.form["comment"]
    return render_template('results.html', name = name, loc = loc, lang = lang, comment = comment)

@app.route('/goBack', methods=['POST'])
def goBack():
    return redirect("/")

app.run(debug=True)