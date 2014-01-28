from .MesFiscal import MesFiscal
from calendar import monthrange
from datetime import datetime

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
