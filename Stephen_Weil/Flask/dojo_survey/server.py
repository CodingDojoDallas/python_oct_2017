from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])
def process_form():
    user_name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('result.html', name=user_name, location=location, language=language, comment=comment)

app.run(debug=True)