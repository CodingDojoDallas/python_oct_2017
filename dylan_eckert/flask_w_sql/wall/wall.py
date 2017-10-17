from flask import Flask, request, redirect, render_template, session, flash
import re, md5, os, binascii
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
app.secret_key = "key"

def curUser():
    query = "SELECT * FROM users WHERE id = :id"
    data = {
    'id' : session['user_id']
    }
    user_list = mysql.query_db(query, data)
    curuser = user_list[0]
    return curuser

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/')

    query = "SELECT * FROM users JOIN posts ON posts.user_id = users.id"
    posts = mysql.query_db(query)

    query = "SELECT * FROM comments JOIN users ON comments.user_id = users.id"
    comments = mysql.query_db(query)

    return render_template('wall.html',all_posts = posts, all_comments = comments, curuser=curUser())


@app.route('/post', methods=['POST'])
def createPost():
    if 'user_id' not in session:
        return redirect('/')

    valid = True

    user = curUser()
    curuser_id = user['id']

    data = {
    'content': request.form['content'],
    'user_id': curuser_id
    }

    #LOGIC FOR POST:
    if len(data['content']) < 2:
        flash("Please enter a valid post")
        valid = False

    if valid:
        query = "SELECT * FROM posts WHERE content=:content"
        posts = mysql.query_db(query, data)

        if len(posts) == 0:
            query = "INSERT INTO posts (content, user_id) VALUES (:content, :user_id)"
            mysql.query_db(query, data)
            flash("Post Submitted!")
        else:
            flash("That post already exists!")

    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def createComment():
    if 'user_id' not in session:
        return redirect('/')

    user = curUser()
    curuser_id = user['id']

    data = {
    'post_id': request.form['postid'],
    'content': request.form['content'],
    'user_id': curuser_id
    }
    print data
    if len(data['content']) < 2:
        flash("Please enter a valid post")

    else:
        query = "INSERT INTO comments (post_id, content, user_id) VALUES (:post_id, :content, :user_id)"
        mysql.query_db(query, data)
        flash("Comment Successful!")

    return redirect('/wall')

@app.route('/register', methods=['POST'])
def register():
    valid = True

    data = {
    'salt': binascii.b2a_hex(os.urandom(15)),
    'username': request.form['username'],
    'password': request.form['password'],
    'pass_conf': request.form['pass_conf'],
    }

    #LOGIC FOR USERNAME:
    if len(data['username']) < 2:
        flash("Please enter a valid username")
        valid = False
    elif not data['username'].isalpha():
        flash("Please use characters a-z")
        valid = False

    #LOGIC FOR PASSWORD and PASS CONF:
    if len(data['password']) < 8:
        flash("Password must be at least 8 characters long")
        valid = False
    elif data['password'] != data['pass_conf']:
        flash("Passwords don't match")
        valid = False

    if valid:
        data['password'] = md5.new(data['password']+data['salt']).hexdigest()
        query = "SELECT * FROM users WHERE username=:username"
        users = mysql.query_db(query, data)

        if len(users) == 0:
            query = "INSERT INTO users (password, username, salt) VALUES (:password, :username, :salt)"
            mysql.query_db(query, data)
            flash("Registration Successful!")
        else:
            flash("That username already exists!")

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    login = {
    'username': request.form['username'].lower(),
    'password': request.form['password']
    }
    query = "SELECT * FROM users WHERE username=:username"
    users = mysql.query_db(query, login)


    if md5.new(login['password']+users[0]['salt']).hexdigest() == users[0]['password']:
        session['user_id'] = users[0]['id']
        return redirect('/wall')
    else:
        flash("Please enter a valid username and password")
        return redirect('/')

app.run(debug=True)
