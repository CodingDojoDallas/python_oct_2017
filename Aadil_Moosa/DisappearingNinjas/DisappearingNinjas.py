from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/ninja/')
# def ninjas():
#     return render_template("ninjas.html", ninja_color="all")

@app.route('/ninja/<ninja_color>')
def getColor(ninja_color):
    print ninja_color
    return render_template("ninjas.html", ninja_color=ninja_color)

app.run(debug=True)