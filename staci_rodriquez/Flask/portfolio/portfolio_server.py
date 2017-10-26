from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')                            
def my_portfolio():
    return render_template('index.html') 

@app.route('/projects')
def projects():
    my_projects = ['Danger Zones', 'Fat Unicorn: The Poopening', 'My Cohort', 'Certify Me, Woof Woof Go!']
    return render_template('projects.html', projects = my_projects)

@app.route('/about')
def about():
    return render_template('about.html')



app.run(debug=True)


#/ anything after the / will be the route to that page 
#def is the method is calling
#render_template means its grabbing that template