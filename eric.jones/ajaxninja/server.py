from flask import Flask, render_template, jsonify, url_for
app = Flask("__name__")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/<color>", methods=["GET"])
def ninja(color):
    if color == "blue":
        img_url = url_for('static', filename='images/leonardo.jpg')
    elif color == "orange":
        img_url = url_for('static', filename='images/michelangelo.jpg')
    elif color == "red":
        img_url = url_for('static', filename='images/raphael.jpg')
    elif color == "purple":
        img_url = url_for('static', filename='images/donatello.jpg')
    return jsonify(img_url=img_url)

app.run(debug=True)
