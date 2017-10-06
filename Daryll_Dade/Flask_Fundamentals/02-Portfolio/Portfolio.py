from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def portfolio():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


app.run(debug=True)
