
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, send_file
from service.scrape_data import get_number
from Adam.Number import Number, Turtle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! 2'


@app.route('/number')
def number():
    return get_number('EUR/USD')

@app.route('/number/<currency>')
def number_currency(currency):
    number = get_number(currency.replace('-', '/'))
    number = Number(number)
    turtle = Turtle(number.binary)
    return send_file('image.gif', mimetype='image/gif')


if __name__ == '__main__':
    app.run()