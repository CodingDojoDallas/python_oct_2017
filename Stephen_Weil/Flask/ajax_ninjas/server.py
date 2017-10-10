from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    color = request.form['color']
    print color
    if color == "Red":
        url = "/static/images/raphael.jpg"
        alt = "Raphael"
        message = "You chose Raphael!"
    elif color == "Blue":
        url = "/static/images/leonardo.jpg"
        alt = "Leonardo"
        message = "You chose Leonardo!"
    elif color == "Orange":
        url = "/static/images/michelangelo.jpg"
        alt = "Michelangelo"
        message = "You chose Michelangelo!"
    elif color == "Purple":
        url = "/static/images/donatello.jpg"
        alt = "Donatello"
        message = "You chose Donatello!"
    return jsonify(url=url, alt=alt, message=message)

app.run(debug=True)