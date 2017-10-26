from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')                            
def landing():
    return render_template('index.html') 

@app.route('/ninjas')
def ninjas():
    ninja_list = ['Zen-like calm', 'Ruthlessness', 'Weapon-savvy', 'Stealth and camouflage', 'Agility', 'Mindfulness']
    return render_template('ninjas.html', ninjas = ninja_list)

@app.route('/dojos', methods = ['POST'])
def dojos():
    print "Dojos info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/')


app.run(debug=True)


