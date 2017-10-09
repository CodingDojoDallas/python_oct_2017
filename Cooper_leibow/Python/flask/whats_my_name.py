from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('name_route.html')

@app.route('/process', methods  = ['POST'])
def process():
    name = request.form['text_box']
    print name
    return redirect ('/')

app.run(debug=True)
