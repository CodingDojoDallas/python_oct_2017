from flask import Flask, render_template, request, redirect, flash, session
app = Flask("__name__")
app.secret_key = "sk"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    formvalid = True
    if len(request.form["name"]) < 1:
        flash("You must enter a name.")
        formvalid = False
    if len(request.form["comment"]) < 1 or len(request.form["comment"]) > 120:
        flash("Your comment must be between 1 and 120 characters.")
        formvalid = False
    if formvalid:
        return render_template("results.html", result=request.form)
    else: 
        return redirect("/")

app.run(debug=True)