#!/usr/bin/python3
# script that starts a Flask web application.

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Prints C followed by <text> contents"""
    text = text.replace("_", " ")
    return 'C {:s}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>')
def python_text(text='is cool'):
    """Prints Python followed by <text> contents"""
    text = text.replace("_", " ")
    return 'Python {:s}'.format(text)


@app.route('/number/<int:n>')
def isNumber(n):
    """displays 'n is number' only if n is an integer"""
    return '{:d} is number'.format(n)


if __name__ == ("__main__"):
    app.run(host="0.0.0.0")
