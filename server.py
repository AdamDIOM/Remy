from flask import Flask
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run()