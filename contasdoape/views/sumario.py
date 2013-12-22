from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user
from contasdoape.models.Tesoureiro import Tesoureiro
from datetime import datetime
from contasdoape import app

@app.route('/sumario', methods=['GET'])
@login_required
def sumario():
    ano = request.args.get('ano') or datetime.now().year

    meses = Tesoureiro().listar_meses(int(ano))
   
    return render_template('sumario.html',
                           usuario = current_user,
                           pessoas = ['Erlan', 'Fernando'], 
                           ano = ano,
                           meses = [mes.obter_sumario() for mes in meses])
