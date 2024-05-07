from flask import Flask, render_template
import random 
from funcoes import *
from random_data import *

app = Flask(__name__)

@app.route("/", methods=("GET",))
def index():
    return render_template("index.html")

from api import bp
app.register_blueprint(bp) 


if __name__ == '__main__':
    app.run(host="0.0.0.0")