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

    def listar_despesas_atuais(self):
        return self._listar_despesas(self._calcular_periodo(datetime.now()))

    def listar_despesas(self, mes, ano):
        data = datetime(year = ano, month = mes, day = 1)
        return self._listar_despesas(self._calcular_periodo(data))

    def calcular_periodo_atual(self):
        return self._calcular_periodo(datetime.now())

    def _listar_despesas(self, periodo):
        data_inicio, data_fim = periodo
        return Despesa.objects(data__gte = data_inicio, data__lte = data_fim)
    
    def _calcular_periodo(self, data):
        days = monthrange(data.year, data.month)
        return (data.replace(day = 1), data.replace(day = days[1]))

    def descobrir_nome_do_periodo(self, periodo):
        meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março', 4 : 'Abril', 
                 5 : 'Maio', 6 : 'Junho', 7 : 'Julho', 8 : 'Agosto', 
                 9 : 'Setembro', 10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro' }
        
        data_inicio = periodo[0]
        return meses[data_inicio.month]
