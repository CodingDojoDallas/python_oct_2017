from flask import Flask, render_template, session, redirect
app = Flask(__name__) #generating an instance of the flask class
app.secret_key = "secretkey" #encrypts and decrypts cookies

@app.route('/')
def counter():
  if 'counter' in session: #counter is just a variable. Session is storing it
    session['counter'] += 1
  else:
    session['counter'] = 1
  return render_template("index.html")

@app.route('/reset') #this is another route to the /reset from the button click in html. Just redirects to the index page but, resets the variable to 0
def counterreset():
  session['counter'] = 0
  return redirect('/')

@app.route('/dos')
def dos():
  session['counter'] += 1 #even though I want it to increment by two, this is adding to the variable once and then the top function will run again adding another one
  return redirect('/')

app.run(debug=True) # run our server