from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "danf1818j3nz"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm_pw']
    birthday = request.form['birthday']
    goodtogo = True
    if len(first_name) < 1:
        flash("First Name field must not be blank!")
        goodtogo = False
    if len(last_name) < 1:
        flash("Last Name field must not be blank!")
        goodtogo = False
    if not EMAIL_REGEX.match(email):
        flash("Not a valid email address!")
        goodtogo = False
    ymd = str(datetime.now())[:10]
    if int(birthday[:4]) >= int(ymd[:4]):
        if int(birthday[:4]) > int(ymd[:4]):
            flash("Birthday must be from the past!")
            goodtogo = False
        elif int(birthday[5:7]) > int(ymd[5:7]):
            flash("Birthday must be from the past!")
            goodtogo = False
        elif birthday[5:7] == ymd[5:7] and int(birthday[8:10]) > int(ymd[8:10]):
            flash("Birthday must be from the past!")
            goodtogo = False
    if len(password) < 9:
        flash("Password not long enough! Must be at least 9 characters.")
        goodtogo = False
    else:
        caps = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if not any(x in password for x in caps) or not any(x in password for x in nums):
            flash("Password must contain at least one capital letter and one number.")
            goodtogo = False
    if password != confirm:
        flash("Password does not match confirmation!")
        goodtogo = False
    if goodtogo:
        flash("Thanks for submitting your information.")
    return redirect('/')

app.run(debug=True)