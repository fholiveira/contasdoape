from bottle import TEMPLATE_PATH, get, post, redirect, request, jinja2_template as template
from app.models.Despesa import Despesa
from app.models.Caixa import Caixa

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
    caixa = Caixa()
    despesas = caixa.listar_despesas_atuais()
    periodo = caixa.calcular_periodo_atual()
    data_inicio, data_fim = periodo

    return template('despesas.html',
                    despesas = [d.to_dict() for d in despesas], 
                    data_inicio = data_inicio.strftime('%d/%m/%Y'), 
                    data_fim = data_fim.strftime('%d/%m/%Y'),
                    mes = caixa.descobrir_nome_do_periodo(periodo) + ' de ' + str(data_inicio.year))
