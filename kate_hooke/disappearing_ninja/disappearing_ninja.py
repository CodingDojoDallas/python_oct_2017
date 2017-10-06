from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing_page_home():
    return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('ninja.html')

@app.route('/ninja/blue')
def blue():
    return render_template('blue.html')

@app.route('/ninja/orange')
def orange():
    return render_template('orange.html')

@app.route('/ninja/red')
def 


app.run(debug=True)