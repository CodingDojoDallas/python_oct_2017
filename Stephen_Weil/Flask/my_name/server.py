from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def get_form():
    user_name = request.form['name']
    print user_name
    return redirect('/')

app.run(debug=True)