from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "My_secret_key"

@app.route('/')
def index():
	# initiate the count
	if 'count' not in session:
		session['count'] = 0
	session['count'] +=1
	return render_template('index.html', count=session['count'])

@app.route('/index', methods=['POST'])
def increment():
	action = request.form['action']
	if action == "2":
		session['count'] += 1
	elif action == "clear":
		session.pop('count')
	return redirect('/')
	
	
app.run(debug=True)
