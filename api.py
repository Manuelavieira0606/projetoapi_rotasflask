from flask import Blueprint, jsonify, request
from funcoes import *
from random_data import *

bp = Blueprint("api", __name__)

@bp.route('/api/', methods=("GET"))
def index():
    return jsonify({"status": 200, "message": "API da Manuela de Lima Ribeiro Vieira"})
@bp.route('/api/aleatorio', methods=("GET"))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route('/api/argumentos/<string:nome>', methods=("GET"))
def argumentos(nome:str):
    return jsonify({"status": 200, "data":nome})

@bp.route('/api/maior50', methods=("GET"))
def maior50():
    return jsonify(maior_de_50(pessoas))

@bp.route('/api/mais2000', methods=("GET"))
def mais2000():
    return jsonify(f'Ganham mais de R$2000 :{mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]} % de {mais_2000(pessoas)[2]} no total')

@bp.route('/api/tresmaioressalarios', methods=("GET"))
def tresmaioressalarios():
    return jsonify(maior_salario(pessoas, maior=None))

@bp.route('/api/mediasalarioprofissao', methods=("GET"))
def mediasalarioprofissao():
    return jsonify(media_profissoes(pessoas))

@bp.route('/api/intervalopessoas2000', methods=("GET"))
def intervalopessoas2000():
    return jsonify(maior_2000_sexo(pessoas, sexo='Masculoino'), maior_2000_sexo(pessoas, sexo='Feminino'))