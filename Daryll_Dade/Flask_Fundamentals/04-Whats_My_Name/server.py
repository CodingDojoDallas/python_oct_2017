from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def Whats_my_name():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    print name
    print name
    return render_template('process.html', name=name)


app.run(debug=True)
