from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "sk"

@app.route("/", methods = ["GET", "POST"])
def randomnum():
    reset = "true"
    if "reset" in request.form:
        reset = request.form["reset"]
    if "target" not in session or reset == "true":
        session["target"] = random.randrange(0, 101)
        session["guess"] = 0
    else:
        session["guess"] = int(request.form["guess"])
    return render_template("index.html")

app.run(debug=True)