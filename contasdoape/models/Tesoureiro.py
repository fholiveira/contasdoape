from .MesFiscal import MesFiscal
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
        pessoas = list(mes_fiscal.obter_despesas())
        despesas_usuario = mes_fiscal.obter_despesas(autor=usuario) 
        valor_gasto = sum(despesa.valor for despesa in despesas_usuario)

        return [self._calcular_divida(valor_gasto, autor, despesas)
                    for autor, despesas in pessoas
                        if autor.id != usuario.id]

    def calcular_divida_relativa(self, mes_fiscal, usuario, amigo):
        valor = sum(depesa.valor for despesa in mes_fiscal.obter_despesas(autor=usuario))
        despesas_amigo = mes_fiscal.obter_despesas(autor=amigo)
        return self._calcular_divida(valor, amigo, despesas_amigo)

    def _calcular_divida(self, valor_base, autor, despesas):
        valor_gasto = sum(despesa.valor for despesa in despesas)
        return {'usuario': autor, 
                'despesas': valor_gasto,
                'divida': valor_base - valor_gasto}
