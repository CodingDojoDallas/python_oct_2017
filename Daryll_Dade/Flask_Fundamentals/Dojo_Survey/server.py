@app.route('/show')
def show_user(:)
    return render_template('user.html', name='Jay',email='kpatel@codingdojo.com')