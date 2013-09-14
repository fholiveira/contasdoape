from bottle import get, redirect, jinja2_template as template
from app.models.Tesoureiro import Tesoureiro
from datetime import datetime

@get('/sumario')
def sumario():
    data = datetime.now()

    meses = Tesoureiro().listar_meses(data.year)
   
    return template('sumario.html',
                    pessoas = ['Erlan', 'Fernando'], 
                    ano = data.year,
                    meses = [mes.obter_sumario() for mes in meses])
