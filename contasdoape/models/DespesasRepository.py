from datetime import datetime
from .Despesa import Despesa 

class DespesaRepository():

    def listar_despesas_do_periodo(self, data_inicio, data_fim):
        self._validar_parametros(data_inicio, data_fim)

        return Despesa.objects(data__gte = data_inicio, 
                               data__lte = data_fim)

    def listar_despesas_da_pessoa(self, data_inicio, data_fim, pessoa):
        self._validar_parametros(data_inicio, data_fim)

        if not isinstance(pessoa, str):
            raise ValueError('pessoa')

        return Despesa.objects(data__gte = data_inicio, 
                               data__lte = data_fim,
                               nome = pessoa)

    def _validar_parametros(self, data_inicio, data_fim):
        if not isinstance(data_inicio, datetime):
            raise ValueError('data_inicio')

        if not isinstance(data_fim, datetime):
            raise ValueError('data_fim')

