from flask.ext.login import login_required, current_user
from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Condominio import Condominio
from flask import render_template, request
from datetime import datetime
from contasdoape.web import app

@app.route('/sumario', methods=['GET'])
@login_required
def sumario():
    ano = request.args.get('ano') or datetime.now().year
    ape = Condominio().obter_ape(current_user)
   
    meses = Tesoureiro(ape).listar_meses(int(ano))
    
    return render_template('sumario.html',
                           usuario = current_user,
                           ano = ano,
                           meses = [(mes.nome_do_mes(), mes.calcular_saldo()) for mes in meses])
