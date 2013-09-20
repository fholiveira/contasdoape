from bottle import TEMPLATE_PATH, get, post, redirect, request, jinja2_template as template
from app.models.Despesa import Despesa
from app.models.Caixa import Caixa
from app.models.Tesoureiro import Tesoureiro
from datetime import datetime

TEMPLATE_PATH.append('./templates')

@get('/despesas/nova')
def home():
    return template('novadespesa.html')

@post('/despesas/nova')
def nova_despesa():
    Caixa().lancar_despesa(data = request.POST.data,
                           autor = request.POST.autor,
                           valor = request.POST.valor,
                           descricao = request.POST.descricao)
    
    redirect('/')

@get('/')
def listar_despesas():
    ano = request.query.ano or datetime.now().year
    mes = request.query.mes or datetime.now().month

    mes_fiscal = Tesoureiro().obter_mes_fiscal(datetime(year=int(ano), month=int(mes), day=1))
    despesas = mes_fiscal.listar_despesas()

    return template('despesas.html',
                    despesas = [d.to_dict() for d in despesas], 
                    data_inicio = mes_fiscal.data_inicio.strftime('%d/%m/%Y'), 
                    data_fim = mes_fiscal.data_fim.strftime('%d/%m/%Y'),
                    mes = mes_fiscal.nome_do_mes() + ' de ' + str(mes_fiscal.data_inicio.year),
                    total = mes_fiscal.calcular_saldo())
