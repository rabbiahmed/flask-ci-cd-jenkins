from flask import Flask
app = Flask(__name__)

# Initializes Flask and defines at least one route
@app.route('/') # The root /
def hello_world():
    return 'This is a simple Flask application. \
        You can use it to automate the build, test, and deployment of a simple web application!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)