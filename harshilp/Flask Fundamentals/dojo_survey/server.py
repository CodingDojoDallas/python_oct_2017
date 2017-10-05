from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def landing():
    return render_template("index.html")
@app.route("/result", methods=['POST'])
def result():
    name = request.form['name']
    loc = request.form['dojo_location']
    lang = request.form['favorite_language']
    comment = request.form["comment"]
    return render_template('results.html', name = name, loc = loc, lang = lang, comment = comment)
@app.route('/goBack', methods=['POST'])
def goBack():
    return redirect("/")

app.run(debug=True)