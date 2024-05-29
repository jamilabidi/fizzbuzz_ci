
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route


def hello_world():
    return 'Hello from Bottle!'


