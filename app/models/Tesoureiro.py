from .MesFiscal import MesFiscal
from datetime import datetime

class Tesoureiro():
    def obter_mes_fiscal(self, data):
        data_inicio, data_fim = self._calcular_periodo(data)
        return MesFiscal(data_inicio, data_fim)
    
    def _calcular_periodo(self, data):
        days = monthrange(data.year, data.month)
        return (data.replace(day = 1), data.replace(day = days[1]))
