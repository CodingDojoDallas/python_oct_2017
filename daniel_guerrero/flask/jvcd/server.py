from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def jean_claude():
	return render_template('jean_claude.html')

@app.route('/kickboxing')
def kickboxing():
	return render_template('kickboxing.html')

@app.route('/bloodsport')
def bloodsport():
	return render_template('bloodsport.html')

@app.route('/goldfish')
def goldfish():
	return render_template('goldfish.html')

@app.route('/splits')
def splits():
	return render_template('splits.html')

@app.route('/drunkdisco')
def drunkdisco():
	return render_template('drunkdisco.html')

@app.route('/kicktrees')
def kicktrees():
	return render_template('kicktrees.html')


app.run(debug=True)


