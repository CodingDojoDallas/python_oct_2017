from flask import Flask, session, redirect, request, render_template
app = Flask(__name__)
app.secret_key = 'sk'

@app.route("/", methods=["POST", "GET"])
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

app.run(debug=True)