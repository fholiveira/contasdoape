from contasdoape.models.Despesa import Despesa
from calendar import monthrange
from datetime import datetime
from time import strptime

class Caixa():
    def lancar_despesa(self, autor, data, valor, descricao = None):
        valor_adaptado = self._adaptar_valor(valor)
        despesa = Despesa(valor_adaptado, autor, self._converter_datetime(data))
        despesa.descricao = descricao

        return despesa.save()

    def _adaptar_valor(self, valor):
        try:
            return float(valor.replace(',', '.'))
        except:
            raise ValueError('valor')

    def _converter_datetime(self, data):
        try:
            return datetime.strptime(data, "%Y-%m-%d")
        except:
            raise ValueError('data')
