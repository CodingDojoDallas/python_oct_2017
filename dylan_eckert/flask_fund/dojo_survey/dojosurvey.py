from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "key"

valid = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    content = {
        "name" : request.form['name'],
        "location" : request.form['location'],
        "language" : request.form['language'],
        "comment" : request.form['comment']
        }

    if len(content['name']) < 1:
        flash("Please enter a name!")
        return redirect('/')
    if len(content['comment']) < 1:
        flash("Please add a comment!")
        return redirect('/')
    elif len(content['comment']) > 120:
        flash("You'r comment is too long!")
        return redirect('/')
    if valid:
        return render_template("results.html", content = content)


app.run(debug=True)
