from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def first():
    return render_template('index.html')
@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("index.html")
app.run(debug=True)
