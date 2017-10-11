import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "nfiao961784gzQ"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/result', methods=['POST'])
def upload_file():
    success = True
    if 'file' not in request.files:
        flash('Your file upload has failed. Please try again.')
        success = False
    file = request.files['file']
    if file.filename == '':
        flash('Your file upload has failed. Please try again.')
        success = False
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        flash('Your file has been successfully uploaded!')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('result.html', success=success)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run(debug=True)