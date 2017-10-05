from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('portfolio.html')

@app.route('/<user>')
def user_handler(user):
    return render_template('index.html', name=user)

app.run(debug=True)