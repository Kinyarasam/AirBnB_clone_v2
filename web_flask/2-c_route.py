#!/usr/bin/python3
# starts a Flask web application.

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """display "Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C {:s}".format(text)
    # return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
