from contasdoape.models.ControleDeAcesso import ControleDeAcesso
from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user
from contasdoape.models.Condominio import Condominio
from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Despesa import Despesa
from contasdoape.web import app
from datetime import datetime

@app.route('/despesas/nova', methods=['GET'])
@login_required
def home():
    return render_template('nova-despesa.html', usuario = current_user)

@app.route('/despesas/nova', methods=['POST'])
@login_required
def nova_despesa():
    ape = Condominio(current_user).obter_ape()
    usuario = ControleDeAcesso().carregar_usuario(current_user.facebook_id)

    despesa = Despesa(autor=usuario,
                      valor=float(request.form['valor'].replace(',', '.')),
                      data=datetime.strptime(request.form['data'], '%Y-%m-%d'))

    despesa.descricao = request.form['descricao']

    ape.incluir_despesa(despesa)

    return redirect(url_for('listar_despesas'))

@app.route('/despesas', methods=['GET'])
@login_required
def listar_despesas():
    ano = request.args.get('ano') or datetime.now().year
    mes = request.args.get('mes') or datetime.now().month

    ape = Condominio(current_user).obter_ape()

    mes_fiscal = Tesoureiro(ape).obter_mes_fiscal(datetime(year=int(ano), month=int(mes), day=1))
    despesas = mes_fiscal.listar_despesas()

    return render_template('despesas.html',
                           ano=ano,
                           mes=mes,
                           usuario = current_user,
                           despesas = despesas, 
                           data_inicio = mes_fiscal.data_inicio, 
                           data_fim = mes_fiscal.data_fim,
                           titulo = mes_fiscal.nome_do_mes() + ' de ' + str(mes_fiscal.data_inicio.year),
                           total = mes_fiscal.calcular_saldo())
