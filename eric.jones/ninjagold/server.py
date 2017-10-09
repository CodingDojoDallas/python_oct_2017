import random
import datetime
from flask import Flask, request, session, redirect, render_template, url_for

app = Flask(__name__)
app.secret_key = "sk"

@app.route("/", methods=["GET", "POST"])
def root():
    if "gold" not in session:
        session["gold"] = 0
        session["activities"] = []
    return render_template("index.html")

@app.route("/process", methods=["GET", "POST"])
def process():
    if "farm" in request.form:
        goldtogive = random.randrange(10, 21)
        session["gold"] += goldtogive
        session["activities"].append("<p><span class='green'>Earned " + str(goldtogive) + " golds on the farm. " + datetime.datetime.now().strftime("%y-%m-%d  %H:%M") + "</span></p>")
    elif "cave" in request.form:
        goldtogive = random.randrange(5, 11)
        session["gold"] += goldtogive
        session["activities"].append("<p><span class='green'>Earned " + str(goldtogive) + " golds in the cave. " + datetime.datetime.now().strftime("%y-%m-%d  %H:%M") + "</span></p>")
    elif "house" in request.form:
        goldtogive = random.randrange(2, 6)
        session["gold"] += goldtogive
        session["activities"].append("<p><span class='green'>Earned " + str(goldtogive) + " golds at home. " + datetime.datetime.now().strftime("%y-%m-%d  %H:%M") + "</span></p>")
    elif "casino" in request.form:
        goldtogive = random.randrange(-50, 51)
        if goldtogive < 0:
            activity = "<p><span class='red'>Lost "
        else:
            activity = "<p><span class='green'>Won "
        session["gold"] += goldtogive
        session["activities"].append(activity + str(goldtogive) + " golds at the casino. " + datetime.datetime.now().strftime("%y-%m-%d  %H:%M") + "</span></p>")
    elif "reset" in request.form:
        session["gold"] = 0
        session["activities"] = []
    return redirect("/")

app.run(debug=True)
