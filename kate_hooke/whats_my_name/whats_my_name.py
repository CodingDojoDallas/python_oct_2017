from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing_page_home():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def create_ninja():
    dojo = request.form['dojo']
    name = request.form['name']
    print name
    email = request.form['email']
    return redirect('/')

app.run(debug=True)