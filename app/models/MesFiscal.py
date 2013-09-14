from .Despesa import Despesa 
from datetime import datetime

class MesFiscal():
    def __init__(self, data_inicio, data_fim):
        self._validar_parametros_de_construcao(data_inicio, data_fim)

        self._data_inicio = data_inicio
        self._data_fim = data_fim

    def _validar_parametros_de_construcao(self, data_inicio, data_fim):
        if not data_inicio or not isinstance(data_inicio, datetime):
            raise ValueError("data_inicio")
        
        if not data_fim or not isinstance(data_fim, datetime):
            raise ValueError("data_fim")

    def listar_despesas(self):
        return Despesa.objects(data__gte = self._data_inicio, self._data__lte = data_fim)
    
    def calcular_saldo(self):
        return Despesa.objects(data__gte = self._data_inicio, self._data__lte = data_fim).sum(valor)
