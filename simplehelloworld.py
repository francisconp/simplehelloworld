#!/usr/bin/python

# Franciscon P. dos Santos
# francisconp@gmail.com

from flask import Flask
from socket import gethostname
from os import environ

app = Flask(__name__)

default_port = environ.get('default_port')

@app.route("/")
def hello():
    var_hostname = gethostname()
    var_msg = 'Teste Container: %s ' % var_hostname
    return var_msg

if default_port != None:
    pass
else:
    print("Please set the default_port environment..")
    exit(1)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=default_port)
