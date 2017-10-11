from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<colorchoice>')
def ninja_color(colorchoice):
    if colorchoice == "blue":
        url_string = "../static/images/leonardo.jpg"
        url_alt = "Leonardo"
    elif colorchoice == "orange":
        url_string = "../static/images/michelangelo.jpg"
        url_alt = "Michelangelo"
    elif colorchoice == "red":
        url_string = "../static/images/raphael.jpg"
        url_alt = "Raphael"
    elif colorchoice == "purple":
        url_string = "../static/images/donatello.jpg"
        url_alt = "Donatello"
    else:
        url_string = "../static/images/notapril.jpg"
        url_alt = "Not April"
    return render_template('ninja.html', url=url_string, alt=url_alt)

app.run(debug=True)