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
    
    redirect('/despesas')

@get('/despesas')
def listar_despesas():
    mes = request.query.mes
    ano = request.query.ano

    despesas = None
    if mes and ano:
        despesas = Caixa().listar_despesas(int(mes), int(ano))
        return template('despesas.html', despesas = [d.to_dict() for d in despesas], ano = ano, mes = mes) 
    else:
        despesas = Caixa().listar_todas_despesas()
        return template('despesas.html', despesas = [d.to_dict() for d in despesas])
