from .Despesa import Despesa
from datetime import datetime
from time import strptime
from calendar import monthrange

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

    def listar_todas_despesas(self):
        return Despesa.objects.all()

    def listar_despesas(self, mes, ano):
        start = datetime(year = ano, month = mes, day = 1)
        end = self._calcular_ultimo_dia_do_mes(start)

        return Despesa.objects(data__gte = start, data__lte = end)


    def _calcular_ultimo_dia_do_mes(self, data):
        days = monthrange(data.year, data.month)
        return data.replace(day=days[1])

