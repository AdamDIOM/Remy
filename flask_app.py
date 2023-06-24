
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from service.scrape_data import get_number

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! 2'


@app.route('/number')
def number():
    return get_number('EUR/USD')

