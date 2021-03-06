from dateutil.relativedelta import relativedelta
from . import MesFiscal, Relatorio
from calendar import monthrange
from datetime import datetime


class Tesoureiro():
    def __init__(self, ape):
        self.ape = ape

    def obter_mes_fiscal(self, mes, ano):
        hoje = datetime.today()
        dia = hoje.day if mes == hoje.month and ano == hoje.year else 15
        data_inicio, data_fim = self._calcular_periodo(datetime(ano, mes, dia))

        return MesFiscal(self.ape, data_inicio, data_fim)

    def _calcular_data_fechamento(self, mes, ano):
        _, ultimo = monthrange(ano, mes)
        dia = self.ape.dia_do_acerto
        dia = dia if dia < ultimo else ultimo
        return datetime(ano, mes, dia)

    def _calcular_periodo(self, data):
        data1 = self._calcular_data_fechamento(data.month, data.year)

        delta = relativedelta(months=1)
        data2 = data1 + delta if data1 < data else data1 - delta
        data2 = self._calcular_data_fechamento(data2.month, data2.year)

        D = relativedelta(days=1)
        return (data1, data2 - D) if data1 < data2 else (data2, data1 - D)

    def listar_meses(self, ano):
        return [self.obter_mes_fiscal(mes, ano) for mes in range(1, 13)]

    def gerar_relatorio(self, mes_fiscal, usuario):
        return Relatorio(mes_fiscal.obter_despesas(), usuario)
