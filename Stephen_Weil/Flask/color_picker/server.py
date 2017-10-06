from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def change_color():
    rval = int(request.form['red'])
    gval = int(request.form['green'])
    bval = int(request.form['blue'])
    ret = render_template('index.html', red=rval, green=gval, blue=bval)
    # adding a fallback for out of bounds values
    # no message but at least won't break
    allvals = [rval, gval, bval]
    for val in allvals:
        if val > 255 or val < 0:
            ret = redirect('/')
    return ret

app.run(debug=True)