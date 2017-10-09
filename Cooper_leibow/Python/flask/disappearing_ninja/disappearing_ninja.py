from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ninja/')
def ninja():
    return render_template("ninja.html", ninja="tmnt" )

@app.route('/ninja/<color>')
def color(color):
    if color == "red":
        return render_template('ninja.html', color="raphael")
    elif color == "blue":
        return render_template('ninja.html', color="leonardo")
    elif color == "orange":
        return render_template('ninja.html', color="michelangelo")
    elif color == "purple":
        return render_template('ninja.html', color="donatello")
    else:
        return render_template('ninja.html', color="notapril")
app.run(debug=True)
