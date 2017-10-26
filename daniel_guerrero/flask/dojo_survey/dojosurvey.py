from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = "my_super_secret_key"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
	session['survey'] = request.form
	return redirect('/result')

@app.route('/result')
def result():
	data = session['survey']

	return render_template('result.html', data=data)


app.run(debug=True)
