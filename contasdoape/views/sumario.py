from flask import render_template, request, redirect, url_for
from contasdoape.models.Tesoureiro import Tesoureiro
from datetime import datetime
from contasdoape import app

@app.route('/sumario', methods=['GET'])
def sumario():
    ano = request.query.ano or datetime.now().year

    meses = Tesoureiro().listar_meses(int(ano))
   
    return template('sumario.html',
                    pessoas = ['Erlan', 'Fernando'], 
                    ano = ano,
                    meses = [mes.obter_sumario() for mes in meses])
