from flask import Flask, jsonify
import random 
from funcoes import *
from random_data import *

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)