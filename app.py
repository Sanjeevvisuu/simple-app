# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a static Flask app.Tested webhook'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
