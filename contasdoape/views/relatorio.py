from flask.ext.login import login_required, current_user
from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Condominio import Condominio
from contasdoape.models.Ape import Ape
from flask import render_template
from contasdoape.web import app
from datetime import datetime


@app.route('/relatorio', defaults={'ano': None, 'mes': None}, methods=['GET'])
@app.route('/relatorio/<int:ano>/<int:mes>', methods=['GET'])
@login_required
def relatorio(ano, mes):
    data = datetime(year=ano if ano else datetime.now().year,
                    month=mes if mes else datetime.now().month,
                    day=1)

    ape = Condominio(current_user).obter_ape()
    tesoureiro = Tesoureiro(ape)
    mes_fiscal = tesoureiro.obter_mes_fiscal(data)
    relatorio = tesoureiro.gerar_relatorio(mes_fiscal, current_user)

    return render_template('relatorio.jinja',
                           ano=data.year,
                           mes=data.month,
                           relatorio=relatorio,
                           nome_mes=mes_fiscal.nome_do_mes())
