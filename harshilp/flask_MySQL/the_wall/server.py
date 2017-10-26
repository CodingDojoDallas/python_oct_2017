from flask import Flask, redirect, render_template, session, flash, request
from mysqlconnection import MySQLConnector
import md5
import re
import os, binascii
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall')
app.secret_key = 'Boo'

def validation():
    error = False
    if len(request.form['first_name']) < 1:
        flash('First name cannot be blank', 'Error:FirstName')
        error = True
    elif request.form['first_name'].isalpha() == False:
        flash('First name must contain only letters', 'Error:FirstName')
        error = True

    if len(request.form['last_name']) < 1:
        flash('Last name cannot be blank', 'Error:LastName')
        error = True
    elif request.form['last_name'].isalpha() == False:
        flash('Last name must contain only letters', 'Error:LastName')
        error = True

    if len(request.form['email']) < 1:
        flash('Email cannot be blank', 'Error:Email')
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address', 'Error:Email')
        error = True

    if len(request.form['password']) < 1:
        flash('Password cannot be blank', 'Error:Password')
        error = True
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 7 characters', 'Error:Password')
        error = True
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Password must contain at least one lowercase, uppercase and digit', 'Error:Password')
        error = True

    if len(request.form['cpassword']) < 1:
        flash('Password confirmation cannot be blank', 'Error:PasswordConfirmation')
        error = True
    elif request.form['password'] != request.form['cpassword']:
        flash('Passwords don\'t match', 'Error:PasswordConfirmation')
        error = True

    return error != True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if validation() == False:
        return redirect('/')
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        salt =  binascii.b2a_hex(os.urandom(15))
        password = request.form['password']
        hashed_pw = md5.new(password + salt).hexdigest()
        query = 'INSERT INTO users(first_name, last_name, email, salt, password, created_by, updated_at) VALUES(:first_name, :last_name, :email,:salt, :password, NOW(), NOW())'
        data = {'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'salt': salt,
                'password': hashed_pw
        }
        new_id = mysql.query_db(query,data)
        session['name'] = '{} {}'.format(data['first_name'], data['last_name'])
        session['id'] = new_id
        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    query = 'SELECT * FROM users where email = :email'
    data = {'email':email}
    valid = mysql.query_db(query,data)

    if len(valid) < 1:
        flash('Not a valid log in ID', 'Error:LoginFirstName')
        return redirect('/')
    else:
        if md5.new(password + valid[0]['salt']).hexdigest() == valid[0]['password']:
            session['name'] = '{} {}'.format(valid[0]['first_name'], valid[0]['last_name'])
            session['id'] = valid[0]['id']
            return redirect('/wall')
        else:
            flash('Password invalid', 'Error:LoginPassword')
            return redirect('/')

@app.route('/wall')
def wall():
    query = 'SELECT message, CONCAT(first_name, " ", last_name) as name, date_format(messages.created_at, \"%M %D, %Y\ %r") as time, messages.id FROM users JOIN messages ON messages.user_id = users.id ORDER BY created_at DESC'
    messages = mysql.query_db(query)

    query = 'SELECT comment, CONCAT(first_name, " ", last_name) as name, date_format(comments.created_at, \"%M %D, %Y\ %r") as time, messages.id, comments.message_id, comments.id FROM users JOIN comments ON users.id = comments.user_id JOIN messages on messages.id = comments.message_id ORDER BY comments.created_at'
    comments = mysql.query_db(query)

    return render_template('wall.html', messages = messages, comments = comments)

@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    query = 'INSERT INTO messages(message, user_id, created_at, updated_at) VALUES(:message, :user_id, NOW(), NOW())'
    data = {
        'message':message,
        'user_id':session['id']
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
    comment = request.form['comment']
    query = 'INSERT INTO comments(comment, user_id, message_id, created_at, updated_at) VALUES(:comment, :user_id, :message_id, NOW(), NOW())'
    data = {
        'comment':comment,
        'user_id':session['id'],
        'message_id':message_id
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/delete/<comment_id>', methods=['POST'])
def delete(comment_id):
    query = 'SELECT created_at FROM comments where comments.id = :comment_id'
    data = {
        'comment_id':comment_id
    }
    date = mysql.query_db(query,data)
    created = date[0]['created_at']
    timesince = datetime.datetime.now() - created
    minutessince = int(timesince.total_seconds() / 60)
    if minutessince < 30:
        query = 'DELETE FROM comments where comments.id = :comment_id'
        mysql.query_db(query,data)
        return redirect('/wall') 
    else:
        flash('Cannot delete comment if more than 30 minutes since posting', 'Error:CommentDelete')
        return redirect('/wall')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)