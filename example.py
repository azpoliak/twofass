from flask import Flask, request, jsonify
from flask import render_template
from pytwofaas import PyTwoFaas

app = Flask(__name__)

@app.route('/') 
def index():
    p = PyTwoFaas("Aklsjdlksajdasl")
    p.init('alskdjalksjd', '1812831283128')
    return 'Index!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)