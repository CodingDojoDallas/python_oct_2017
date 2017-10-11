from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "aisdjfs897afasjoi1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])
def process_form():
    user_name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    ret = render_template('result.html', name=user_name, location=location, language=language, comment=comment)
    if len(user_name) < 1:
        flash("Name field must not be blank!")
        ret = redirect('/')
    if len(comment) < 1:
        flash("Comment field must not be blank!")
        ret = redirect('/')
    elif len(comment) > 120:
        flash("Comment may not be longer than 120 characters!")
        ret = redirect('/')
    return ret

app.run(debug=True)