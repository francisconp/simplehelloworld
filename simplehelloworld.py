from flask import Flask
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def hello():
    var_hostname = gethostname()
    var_msg = 'Teste Container: %s ' % var_hostname
    return var_msg

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8000')
