from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def noninjas():
    return render_template("ninjas.html", display="none")

@app.route("/ninjas", methods=['GET', 'POST'])
def allninjas():
    return render_template("ninjas.html", display="all")

@app.route("/ninjas/<color>", methods=['GET', 'POST'])
def oneninja(color):
    return render_template("ninjas.html", display=color)

app.run(debug=True)