from flask import Flask

# AWS looks for 'application' callable by default
application = Flask(__name__)

@application.route('/')
def hello():
    return ' Hello from CKT! This is my first cloud app on AWS.'

if __name__ == '__main__':
    application.run(debug=True)