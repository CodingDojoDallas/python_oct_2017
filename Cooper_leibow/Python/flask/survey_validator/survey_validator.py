from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "whyy"

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def error():
    print len(request.form['name'])
    if int(len(request.form['name'])) > 1:
        flash("Success! Your name is {}".format(request.form['name']))
    else: 
        flash("Name cant be empty!!")
        return redirect ('/')
    if len(request.form['comment']) < 120:
        flash("Success. You can count!")
    else:
        flash("You fail. You cant have more than 120 characters")
        return redirect('/')
    return (results())
def results():
    print request.form['name']
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html', name = name, language = language, location = location, comment = comment)
app.run(debug=True)