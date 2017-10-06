from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html')
    return redirect('/')


@app.route('/ninjas')
def ninjas_page():
    return render_template('/ninjas.html')
    return redirect('/')


@app.route('/blue')
def blue():
    return render_template('/blue.html')
    return redirect('/')


@app.route('/orange')
def orange():
    return render_template('/orange.html')
    return redirect('/')


@app.route('/purple')
def purple():
    return render_template('/purple.html')
    return redirect('/')


@app.route('/red')
def red():
    return render_template('/red.html')
    return redirect('/')


@app.route('/notarpil')
def notapril():
    return render_template('/notapril.html')
    return redirect('/')


app.run(debug=True)
