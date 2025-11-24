from flask import Flask
app = Flask(__name__)

# Initializes Flask and defines at least one route
@app.route('/') # The root /
def hello_world():
    return 'This is a simple Flask application. \
        This can be used to automate the build, test, and deployment of a simple web application!'
