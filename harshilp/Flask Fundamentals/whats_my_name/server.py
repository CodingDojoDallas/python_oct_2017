from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    print "Got post information"
    print "Users name is {}".format(request.form['name'])
    return redirect('/')

app.run(debug=True)