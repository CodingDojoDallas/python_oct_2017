from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)