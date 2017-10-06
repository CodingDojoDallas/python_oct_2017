from flask import Flask, render_template         
app = Flask(__name__)


@app.route('/')
def Home_page():
    return render_template('index.html', content='Aadil')

@app.route('/projects')
def Projects():
    return render_template('projects.html' )

@app.route('/about')
def About():
    return render_template('about.html' )

app.run(debug=True)             