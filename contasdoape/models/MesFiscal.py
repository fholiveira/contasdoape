from contasdoape.models.Despesa import Despesa 
from datetime import datetime

class MesFiscal():
    def __init__(self, ape, data_inicio, data_fim):
        params = {'data_inicio' : data_inicio, 
                  'data_fim' : data_fim 
                  'ape' : ape}

        for key, value in params.items():
            if not value: raise ValueError(key)

        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.ape = ape

    def listar_despesas(self):
        return [despesa in ape.despesas 
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

    def gastos_por_pessoa(self):
        despesas = self.listar_despesas()
        lista = {}

        for despesa in despesas:
            lista[despesa.autor.nome] += despesa.valor

    def obter_sumario(self):
        autores = self.gastos_por_pessoa()

        sumario = { 'nome' : self.nome_do_mes(),
                    'total' : '%.2f' % self.calcular_saldo()}

        sumario.update(autores)

        return sumario
