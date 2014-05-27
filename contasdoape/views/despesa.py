from contasdoape.models import Condominio, Tesoureiro, Despesa, ControleDeAcesso
from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user
from contasdoape.web import app
from datetime import datetime


@app.route('/despesas/nova', methods=['GET'])
@login_required
def home():
    return render_template('nova-despesa.jinja', usuario=current_user)


@app.route('/despesas/nova', methods=['POST'])
@login_required
def nova_despesa():
    ape = Condominio(current_user).obter_ape()
    usuario = ControleDeAcesso().carregar_usuario(current_user.facebook_id)

    data = None
    try:
        data = datetime.strptime(request.form['data'], '%Y-%m-%d')
    except:
        data = datetime.strptime(request.form['data'], '%d/%m/%Y')

    despesa = Despesa(autor=usuario,
                      valor=float(request.form['valor'].replace(',', '.')),
                      data=data)

    despesa.descricao = request.form['descricao']

    ape.incluir_despesa(despesa)

    return redirect(url_for('listar_despesas'))


@app.route('/despesas/excluir/<fb_id>', methods=['POST'])
@login_required
def excluir_despesa(fb_id):
    ape = Condominio(current_user).obter_ape()
    hoje = datetime.now().date()

    mes_fiscal = Tesoureiro(ape).obter_mes_fiscal(hoje.month, hoje.year)
    mes_fiscal.remover_despesa(current_user, fb_id)

    return 'Ok', 200


@app.route('/despesas', defaults={'ano': None, 'mes': None}, methods=['GET'])
@app.route('/despesas/<int:ano>/<int:mes>', methods=['GET'])
@login_required
def listar_despesas(ano, mes):
    ape = Condominio(current_user).obter_ape()
    hoje = datetime.now()

    mes_fiscal = Tesoureiro(ape).obter_mes_fiscal(mes or hoje.month,
                                                  ano or hoje.year)
    despesas = mes_fiscal.listar_despesas()

    return render_template('despesas.jinja',
                           ano=ano or hoje.year,
                           mes=mes or hoje.month,
                           despesas=despesas,
                           data_inicio=mes_fiscal.data_inicio,
                           data_fim=mes_fiscal.data_fim,
                           titulo=mes_fiscal.nome_do_mes() + ' de ' + str(mes_fiscal.data_inicio.year),
                           total=mes_fiscal.calcular_saldo())
