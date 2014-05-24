from flask.ext.login import login_required, current_user
from contasdoape.models import Tesoureiro, Condominio
from flask import render_template, request
from contasdoape.web import app
from datetime import datetime


@app.route('/sumario', defaults={'ano': None}, methods=['GET'])
@app.route('/sumario/<int:ano>', methods=['GET'])
@login_required
def sumario(ano):
    ape = Condominio(current_user).obter_ape()
    meses = Tesoureiro(ape).listar_meses(ano if ano else datetime.now().year)

    return render_template('sumario.jinja',
                           ano=ano if ano else datetime.now().year,
                           meses=meses)
