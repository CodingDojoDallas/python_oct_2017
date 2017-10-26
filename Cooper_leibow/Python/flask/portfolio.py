from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my crib. My name is Cooper!"

@app.route('/about')
def about():
    return render_template('about_me.html')

@app.route('/projects')
def my_projects():
    return render_template("my_projects.html")

app.run(debug=True)
