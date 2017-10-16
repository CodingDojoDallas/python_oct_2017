from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "nasbu76q2123mf"
mysql = MySQLConnector(app, 'booksdb')

@app.route('/')
def index():
    query = "SELECT * FROM books"
    books = mysql.query_db(query)
    return render_template('index.html', books=books)

@app.route('/book/add/')
def add_book_page():
    return render_template('addbook.html')

@app.route('/book/create/', methods=['post'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    if len(title) < 2 or len(author) < 2:
        flash('Title and Author must be at least 2 characters.')
        return redirect('/book/add')
    else:
        query = "INSERT INTO books (title, author, added_at) VALUES (:title, :author, NOW());"
        data = {
            'title': title,
            'author': author
        }
        mysql.query_db(query, data)
        return redirect('/')

@app.route('/delete/<bookid>/')
def delete_confirmation(bookid):
    query = "SELECT title FROM books WHERE id = :id"
    data = {'id': bookid}
    book = mysql.query_db(query, data)
    return render_template('delete.html', book=book[0], bookid=bookid)

@app.route('/remove/<bookid>/')
def remove_book(bookid):
    query = "DELETE FROM books WHERE id = :id"
    data = {'id': bookid}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/quotes/<bookid>/')
def show_quotes(bookid):
    query = "SELECT books.title AS title, quotes.content AS content FROM quotes " +\
            "JOIN books ON books.id = quotes.book_id " +\
            "WHERE books.id = :id;"
    data = {'id': bookid}
    quotes = mysql.query_db(query, data)
    return render_template('quotes.html', quotes=quotes)

@app.route('/quotes/add/<bookid>/')
def add_quotes_page(bookid):
    query = "SELECT title, id FROM books WHERE id = :id"
    data = {'id': bookid}
    title = mysql.query_db(query, data)
    return render_template('addquote.html', title=title[0])

@app.route('/quote/create/<bookid>/', methods=['post'])
def create_quote(bookid):
    if len(request.form['quote']) < 1:
        flash("Quote text may not be empty!")
        url = '/quotes/add/' + bookid
        return redirect(url)
    query = "INSERT INTO quotes (content, book_id) VALUES (:content, :id)"
    data = {
        'content': request.form['quote'],
        'id': bookid
    }
    mysql.query_db(query, data)
    url = "/quotes/" + bookid
    return redirect(url)

app.run(debug=True)