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
        gastos_por_pessoa = { pessoa : sum(d.valor for d in despesas)
                                for pessoa, despesas in mes_fiscal.obter_despesas().items() }

        total = sum(gasto for pessoa, gasto in gastos_por_pessoa.items())
        valor_medio = total / len(gastos_por_pessoa)
        valor_gasto = next((g for p, g in gastos_por_pessoa.items() if p.id == usuario.id), 0) 

        if valor_gasto > valor_medio:
            gastos_por_pessoa = { pessoa : gastos for pessoa, gastos in gastos_por_pessoa.items() 
                                    if gastos < valor_medio }
        elif valor_gasto < valor_medio:
            gastos_por_pessoa = { pessoa : gastos for pessoa, gastos in gastos_por_pessoa.items() 
                                    if gastos > valor_medio }
        return {'devedor' : valor_gasto < valor_medio,
                'valor_gasto' : valor_gasto,
                'valor_medio' : valor_medio,
                'valor_total' : total,
                'contas' : gastos_por_pessoa }
