from flask import Flask  # Import class Flask (its got a capital "F")to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module. App is an instance of Flask
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return 'Hello World!'  # Return the string 'Hello World!' as a response.
app.run(debug=True)      # Run the app in debug mode.
