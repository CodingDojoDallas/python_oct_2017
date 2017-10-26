from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii
from datetime import datetime
import time

app = Flask(__name__)
app.secret_key = "nasbu76q2123mf"
mysql = MySQLConnector(app, 'thewall')
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
    
    # go register in database
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
            ret = redirect('/wall')
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
                ret = redirect('/wall')
            else:
                flash("Invalid password - did not match!", "login_pw")
        else:
            flash("That email has not been registered!", "login_email")
    return ret

@app.route('/wall')
def success():
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_info = mysql.query_db("SELECT * FROM users WHERE id = :id", {'id': session['user_id']})
        query = "SELECT messages.id, messages.message, DATE_FORMAT(messages.created_at, '%M' ' %D' ' %Y' ' - ' '%l' ':' '%i' ' %p') AS posted, " +\
                "users.id as user_id, CONCAT_WS(' ', users.first_name, users.last_name) AS user_name FROM messages " +\
                "JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
        messages = mysql.query_db(query)
        query_comments = "SELECT comments.id, comments.comment, DATE_FORMAT(comments.created_at, '%M' ' %D' ' %Y' ' - ' '%l' ':' '%i' ' %p') AS posted, " +\
                        "users.id, CONCAT_WS(' ', users.first_name, users.last_name) AS user_name, comments.message_id FROM comments " +\
                        "JOIN users ON comments.user_id = users.id " +\
                        "JOIN messages ON comments.message_id = messages.id ORDER BY comments.created_at"
        comments = mysql.query_db(query_comments)
        return render_template('wall.html', user_info=user_info[0], messages=messages, comments=comments)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/post', methods=['post'])
def post_message():
    if 'user_id' in session and len(request.form['message']) > 0:
        query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES " +\
                "(:content, NOW(), NOW(), :id);"
        data = {
            'content': request.form['message'],
            'id': session['user_id']
        }
        mysql.query_db(query, data)
    else:
        flash("Your post failed. Please make sure you are logged in and that your message contains text.", "post")
    return redirect('/wall')

@app.route('/comment', methods=['post'])
def post_comment():
    if 'user_id' in session and len(request.form['comment']) > 0:
        if len(request.form['comment']) <= 255:
            query = "INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) " +\
                    "VALUES (:content, NOW(), NOW(), :message_id, :user_id);"
            data = {
                'content': request.form['comment'],
                'user_id': session['user_id'],
                'message_id': request.form['messageid']
            }
            mysql.query_db(query, data)
        else:
            flash("Comments are limited to 255 characters.", "comment")
            session['message'] = int(request.form['messageid'])
    else:
        flash("Your comment failed. Please make sure you are logged in and that your comment contains text.", "comment")
        session['message'] = int(request.form['messageid'])
    return redirect('/wall')

@app.route('/delete/<id>')
def delete_post(id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        query = "SELECT messages.user_id, messages.created_at FROM messages WHERE messages.id = :id"
        data = {'id': id}
        proper_user = mysql.query_db(query, data)
        # get times, convert to unix timestamp
        now = time.mktime(datetime.now().timetuple())
        post_time = time.mktime(proper_user[0]['created_at'].timetuple())
        # get difference in seconds, divide by 60 to get minutes
        time_diff = int(now-post_time)/60
        if session['user_id'] == proper_user[0]['user_id'] and time_diff <= 30:
            query = "DELETE FROM messages WHERE messages.id = :id"
            mysql.query_db(query, data)
            flash("You successfully deleted your post!", "delete")
        elif session['user_id'] != proper_user[0]['user_id']:
            flash("Stop trying to cheat the system! You don't have authorization to delete that post.", "delete")
        else:
            flash("Sorry, you may only delete posts that are less than 30 minutes old.", "delete")
        return redirect('/wall')

app.run(debug=True)