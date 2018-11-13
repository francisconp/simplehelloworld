#!/usr/bin/python

# Franciscon P. dos Santos
# francisconp@gmail.com

from flask import Flask, render_template
from socket import gethostname
from os import environ

app = Flask(__name__)

default_port = environ.get('default_port')
default_label = environ.get('default_label')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/")
def root():
    var_hostname = gethostname()
    msgs = { "hostname" : var_hostname,
             "label": default_label,
             "port": default_port }
    return render_template('index.html', msgs=msgs)

@app.route("/hostname")
def hostname():
    var_hostname = gethostname()
    return var_hostname

if default_port != None:
    pass
else:
    print("Please set the default_port environment..")
    exit(1)

if default_label != None:
    pass
else:
    print("Please set the default_label environment..")
    exit(1)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(default_port),debug=True)
