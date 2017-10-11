from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/projects')
def project_page():
    return render_template('project.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

app.run(debug=True)