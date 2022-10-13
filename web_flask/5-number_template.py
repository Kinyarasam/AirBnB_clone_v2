#!/usr/bin/python3
""" Starts a Flask web app

Routes:
    / - displays "Hello HBNB!"
    /hbnb - displays "HBNB"
    /c/<text> - displays "C <text>"
    /python/<text> - displays "Python is cool"
    /number/<n> - displays n if integer
    /number_template/<n> - displays a HTML page if n is int
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Prints C followed by <text> content"""
    text = text.replace("_", " ")
    return 'C {:s}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """Prints Python followed by <text> content"""
    text = text.replace("_", " ")
    return 'Python {:s}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """displays 'n is number' only if n is an integer"""
    return '{:d} is number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """display a HTML page only if n is an integer:"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
