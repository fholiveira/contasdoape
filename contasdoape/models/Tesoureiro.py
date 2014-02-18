from contasdoape.models.MesFiscal import MesFiscal
from contasdoape.models.Divida import Divida
from calendar import monthrange
from datetime import datetime
from itertools import groupby

class Tesoureiro():
    def __init__(self, ape):
        self.ape = ape

    def obter_mes_fiscal(self, data):
        data_inicio, data_fim = self._calcular_periodo(data)
        return MesFiscal(self.ape, data_inicio, data_fim)

    def _calcular_periodo(self, data):
        days = monthrange(data.year, data.month)
        return (data.replace(day = 1), data.replace(day = days[1]))

    def listar_meses(self, ano):
        data = datetime(ano, 1, 1)
        meses = range(1, 13)
        return [self.obter_mes_fiscal(data.replace(month = mes)) for mes in meses]

    def calcular_divida(self, mes_fiscal, usuario):
        return Divida(mes_fiscal.obter_despesas(), usuario)
