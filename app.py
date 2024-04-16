from flask import Flask, jsonify
import random 
from funcoes import *
from random_data import *

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API da Manuela de Lima Ribeiro Vieira"})
@app.route('/aleatorio')
def aleatorios():
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route('/argumentos/<string:nome>')
def argumentos(nome:str):
    return jsonify({"status": 200, "data":nome})

@app.route('/maior50')
def maior50():
    return jsonify(maior_de_50(pessoas))

@app.route('/mais2000')
def mais2000():
    return jsonify(f'Ganham mais de R$2000 :{mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]} % de {mais_2000(pessoas)[2]} no total')

@app.route('/tresmaioressalarios')
def tresmaioressalarios():
    return jsonify(maior_salario(pessoas, maior=None))

@app.route('/mediasalarioprofissao')
def mediasalarioprofissao():
    return jsonify(media_profissoes(pessoas))

@app.route('/intervalopessoas2000')
def intervalopessoas2000():
    return jsonify(maior_2000_sexo(pessoas, sexo='Masculoino'), maior_2000_sexo(pessoas, sexo='Feminino'))


if __name__ == '__main__':
    app.run(debug=True)