from flask import render_template, request, redirect, url_for
from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Despesa import Despesa
from contasdoape.models.Caixa import Caixa
from datetime import datetime
from contasdoape import app

@app.route('/despesas/nova', methods=['GET'])
def home():
    return render_template('novadespesa.html')

@app.route('/despesas/nova', methods=['POST'])
def nova_despesa():
    Caixa().lancar_despesa(data = request.form['data'],
                           autor = request.form['autor'],
                           valor = request.form['valor'],
                           descricao = request.form['descricao'])
    
    return redirect(url_for('listar_despesas'))

@app.route('/', methods=['GET'])
def listar_despesas():
    ano = request.args.get('ano') or datetime.now().year
    mes = request.args.get('mes') or datetime.now().month

    mes_fiscal = Tesoureiro().obter_mes_fiscal(datetime(year=int(ano), month=int(mes), day=1))
    despesas = mes_fiscal.listar_despesas()

    return render_template('despesas.html',
                           despesas = [d.to_dict() for d in despesas], 
                           data_inicio = mes_fiscal.data_inicio.strftime('%d/%m/%Y'), 
                           data_fim = mes_fiscal.data_fim.strftime('%d/%m/%Y'),
                           mes = mes_fiscal.nome_do_mes() + ' de ' + str(mes_fiscal.data_inicio.year),
                           total = mes_fiscal.calcular_saldo())