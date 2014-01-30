from contasdoape.models.Despesa import Despesa 
from datetime import datetime
from itertools import groupby

class MesFiscal():
    def __init__(self, ape, data_inicio, data_fim):
        params = {'data_inicio' : data_inicio, 
                  'data_fim' : data_fim, 
                  'ape' : ape}

        for key, value in params.items():
            if not value: raise ValueError(key)

        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.ape = ape

    def listar_despesas(self):
        return [despesa for despesa in self.ape.despesas
                    if despesa.data >= self.data_inicio and 
                       despesa.data <= self.data_fim]

    def calcular_saldo(self):
        despesas = self.listar_despesas()
        return sum(d.valor for d in despesas)

    def nome_do_mes(self):
        meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março', 4 : 'Abril', 
                 5 : 'Maio', 6 : 'Junho', 7 : 'Julho', 8 : 'Agosto', 
                 9 : 'Setembro', 10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro' }
        
        return meses[self.data_inicio.month]

    def obter_despesas(self, autor=None):
        despesas_do_mes = self.listar_despesas()
        despesas_por_autor = groupby(despesas_do_mes, 
                                     lambda despesa : despesa.autor)
        if autor:
            return next(list(despesas) for usuario, despesas in despesas_por_autor 
                        if usuario.id == autor.id )

        return [(autor, list(despesas)) for autor, despesas in despesas_por_autor]

    def obter_sumario(self):
        autores = self.gastos_por_pessoa()

        sumario = { 'nome' : self.nome_do_mes(),
                    'total' : 'R$ {0:.2f}'.format(self.calcular_saldo())}

        sumario.update(autores)

        return sumario
