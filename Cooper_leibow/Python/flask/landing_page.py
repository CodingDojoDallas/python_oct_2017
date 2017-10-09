from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hi there. How're you doing?"

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def newSend():
    return render_template('dojos_new.html')

app.run(debug=True)
