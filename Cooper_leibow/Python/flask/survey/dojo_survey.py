from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('survey_root.html')

@app.route('/result', methods=['POST'])
def results():
    print request.form['name']
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('survey_result.html', name = name)
app.run(debug=True)
