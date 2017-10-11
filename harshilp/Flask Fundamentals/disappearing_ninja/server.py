from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def landing():
    return render_template("index.html")
@app.route("/ninja")
def ninja():
    return render_template('ninja.html')
@app.route('/ninja/<ninja_color>')
def color(ninja_color):
    turtle = 'notapril'
    if ninja_color == "blue":
        turtle = 'leonardo'
    elif ninja_color == "red":
        turtle = "raphael"
    elif ninja_color == "orange":
        turtle = "michelangelo"
    elif ninja_color == 'purple':
        turtle = "donatello"
    print turtle
    return render_template('ninjaColor.html', turtle = turtle)
app.run(debug=True)