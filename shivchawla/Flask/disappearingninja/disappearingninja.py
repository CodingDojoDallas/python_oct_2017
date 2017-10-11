from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def all():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        return render_template('ninjas.html',color="leonardo") #left hand side is html, right is value
    elif color == "red":
        return render_template('ninjas.html',color="raphael")
    elif color == "purple":
        return render_template('ninjas.html',color="donatello")
    elif color == "orange":
        return render_template('ninjas.html',color="michelangelo")
    else:
        return render_template('ninjas.html',color="notapril")
app.run(debug=True)