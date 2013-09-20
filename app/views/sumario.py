from bottle import get, redirect, request, jinja2_template as template
from app.models.Tesoureiro import Tesoureiro
from datetime import datetime

@get('/sumario')
def sumario():
    ano = request.query.ano or datetime.now().year

    meses = Tesoureiro().listar_meses(int(ano))
   
    return template('sumario.html',
                    pessoas = ['Erlan', 'Fernando'], 
                    ano = ano,
                    meses = [mes.obter_sumario() for mes in meses])
