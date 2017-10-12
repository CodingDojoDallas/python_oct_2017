from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii

app = Flask(__name__)
app.secret_key = "nasbu76q2123mf"
mysql = MySQLConnector(app, 'logindb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['post'])
def register():
    # set some variables to store data
    # will add password to data later after hashing
    ret = redirect('/')
    data = {
        'first': request.form['first'],
        'last': request.form['last'],
        'email': request.form['email'],
    }
    pword = request.form['pword']
    goodtogo = True
    
    # check if fields are empty
    if len(data['first']) < 2 or not data['first'].isalpha() or len(data['last']) < 2 or not data['last'].isalpha():
        flash("Names must be at least 2 characters and consist only of letters!", "reg_name")
        goodtogo = False
    
    # check if email is valid
    if not EMAIL_REGEX.match(data['email']):
        flash("Not a valid email address!", "reg_email")
        goodtogo = False
    
    # check if password 8 characters and matches
    if len(pword) < 8:
        flash("Your password must be at least 8 characters!", "reg_pw")
        goodtogo = False
    if pword != request.form['confirm']:
        flash("Your password and confirmation did not match!", "reg_conf")
        goodtogo = False
    if goodtogo:
        # check if email already used
        current_emails = mysql.query_db("SELECT email FROM users")
        if any(x['email'] == data['email'] for x in current_emails):
            flash("Your email is already taken!", 'reg_email')
        else:
            # hashing up the pw
            salt = binascii.b2a_hex(os.urandom(15))
            hashed_pw = md5.new(request.form['pword'] + salt).hexdigest()
            data['salt'] = salt
            data['pword'] = hashed_pw
            query = "INSERT INTO users (first_name, last_name, email, pword, salt, created_at, updated_at) " +\
                    "VALUES (:first, :last, :email, :pword, :salt, NOW(), NOW());"
            user_id = mysql.query_db(query, data)
            flash("You successfully registered your account!", "register")
            session['user_id'] = user_id
            ret = redirect('/success')
    # return
    return ret

@app.route('/login', methods=['post'])
def login():
    data = {
        'email': request.form['email'],
        'pword': request.form['pword']
    }
    goodtogo = True
    ret = redirect('/')
    if len(data['pword']) < 8:
        flash("Invalid password - must be at least 8 characters.", "login_pw")
        goodtogo = False
    if not EMAIL_REGEX.match(data['email']):
        flash("Invalid email - must be string@string.string", "login_email")
        goodtogo = False
    if goodtogo:
        # check if user email is in db
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_info = mysql.query_db(query, data)
        print user_info
        if len(user_info) != 0:
            user_info = user_info[0]
            encrypted_password = md5.new(data['pword'] + user_info['salt']).hexdigest()
            if user_info['pword'] == encrypted_password:
                session['user_id'] = user_info['id']
                ret = redirect('/success')
            else:
                flash("Invalid password - did not match!", "login_pw")
        else:
            flash("That email has not been registered!", "login_email")
    return ret

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    else:
        query = "SELECT * FROM users WHERE id = :id"
        data = {'id': session['user_id']}
        user_info = mysql.query_db(query, data)
        return render_template('success.html', user_info=user_info[0])

app.run(debug=True)