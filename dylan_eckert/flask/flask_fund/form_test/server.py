from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/users/<username>/<id>')
# As you can see, the route itself has a placeholder after the '/users/'. The placeholder is designated in <> tags where the name inside of the tags should match the parameter name that is passed to the route handler function.
def show_user_profile(username, id):
    print username
    print id
    return render_template("users.html", name="Dylan")

app.run(debug=True)
