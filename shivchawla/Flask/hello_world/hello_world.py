from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                        # routes are shit that comes after the slash of a URL
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.

@app.route('/success')
def success():
  return render_template('success.html')

app.run(debug=True)      # Run the app in debug mode.