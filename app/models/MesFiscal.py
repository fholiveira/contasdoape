from .Despesa import Despesa 
from datetime import datetime

class MesFiscal():
    def __init__(self, data_inicio, data_fim):
        self._validar_parametros_de_construcao(data_inicio, data_fim)

        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def _validar_parametros_de_construcao(self, data_inicio, data_fim):
        if not data_inicio or not isinstance(data_inicio, datetime):
            raise ValueError("data_inicio")
        
        if not data_fim or not isinstance(data_fim, datetime):
            raise ValueError("data_fim")

    def listar_despesas(self):
        return Despesa.objects(data__gte = self.data_inicio, data__lte = self.data_fim)
    
    def calcular_saldo(self):
        return Despesa.objects(data__gte = self.data_inicio, data__lte = self.data_fim).sum('valor')
    
    def nome_do_mes(self):
        meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março', 4 : 'Abril', 
                 5 : 'Maio', 6 : 'Junho', 7 : 'Julho', 8 : 'Agosto', 
                 9 : 'Setembro', 10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro' }
        
        return meses[self.data_inicio.month]

    def obter_autores(self):
        return Despesa.objects(data__gte = self.data_inicio, 
                               data__lte = self.data_fim).distinct('nome')


    def calcular_saldo_por_autor(self, autor):
        return Despesa.objects(data__gte = self.data_inicio, 
                               data__lte = self.data_fim, 
                               nome = autor).sum('valor')

    def obter_sumario(self):
        sumario = {'nome' : self.nome_do_mes(),
                   'total' : self.calcular_saldo()}

        for autor in self.obter_autores():
            sumario[autor] = self.calcular_saldo_por_autor(autor)

        return sumario

