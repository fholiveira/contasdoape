from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user
from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Ape import Ape 
from contasdoape.models.Condominio import Condominio
from contasdoape.web import app
from datetime import datetime

@app.route('/relatorio/<ano>/<mes>', methods=['GET'])
@login_required
def relatorio(ano, mes):
    ape = Condominio(current_user).obter_ape()

    tesoureiro = Tesoureiro(ape)
    mes_fiscal = tesoureiro.obter_mes_fiscal(datetime(int(ano), int(mes), 1))

    divida = tesoureiro.calcular_divida(mes_fiscal, current_user) 

    return render_template('relatorio.html',
                           valor_gasto=divida.valor_gasto_pelo_usuario(),
                           valor_medio=divida.valor_medio(),
                           valor_total=divida.valor_total(),
                           contas=divida.divida_relativa(),
                           devedor=divida.usuario_esta_devendo(),
                           nome_mes=mes_fiscal.nome_do_mes(),
                           ano=ano,
                           mes=mes)

