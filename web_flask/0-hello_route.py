#!/usr/bin/python3
# Starts a Flask web application:

from flask import Flask

app = Flask(__name__)

"""Documentation"""
@app.route('/', strict_slashes=False)
def hello():
    """Displays the message Hello HBNB!"""
    return 'Hello HBNB!'

"""Run server on port 5000"""
if __name__ == "__main__":
    app.run(host="0.0.0.0")
