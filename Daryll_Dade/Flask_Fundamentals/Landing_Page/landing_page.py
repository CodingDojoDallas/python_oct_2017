from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')


def ninjas():
    return render_template('ninjas')

def dojos():
    return render_template('dojos.html')



app.run(debug=True)
