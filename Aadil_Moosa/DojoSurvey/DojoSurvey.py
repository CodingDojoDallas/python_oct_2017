from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    content = {
        "name" : request.form['name'],
        "location" : request.form['location'],
        "language" : request.form['language'],
        "comment" : request.form['comment'],
        }
    return render_template("results.html", content = content)


app.run(debug=True)












# from flask import Flask, render_template, request, redirect, session   
# app = Flask(__name__)
# app.secret_key = "BonelessPizza"

# @app.route('/')
# def home_page():
#     location_list = ['Dallas', 'San Jose', 'New York', 'Seattle']
#     language_list = ['Python', 'English', 'Javascript', 'HTML']
#     return render_template('index.html', location_list=location_list, language_list=language_list)

# @app.route('/process', methods=['POST'])
# def index_form():
#     session['name'] = request.form['name']
#     session['location'] = request.form['location']
#     session['language'] = request.form['language']
#     session['comment'] = request.form['comment']
#     return redirect('/results')


# @app.route('/results')
# def results_page():
#     return render_template('results.html')

# app.run(debug=True)