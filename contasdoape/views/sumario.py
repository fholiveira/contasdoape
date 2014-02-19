from flask.ext.login import login_required, current_user
from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Condominio import Condominio
from flask import render_template, request
from datetime import datetime
from contasdoape.web import app

@app.route('/sumario', defaults={'ano': None}, methods=['GET'])
@app.route('/sumario/<int:ano>', methods=['GET'])
@login_required
def sumario(ano):
    ape = Condominio(current_user).obter_ape()
    meses = Tesoureiro(ape).listar_meses(ano if ano else datetime.now().year)
    
    return render_template('sumario.html',
                           ano=ano if ano else datetime.now().year,
                           meses=[(mes.nome_do_mes(), mes.calcular_saldo()) for mes in meses])
