from .DespesasRepository import DespesaRepository
from .GrupoFiscal import GrupoFiscal
from datetime import datetime
from .Despesa import Despesa 

class MesFiscal():
    def __init__(self, data_inicio, data_fim):
        params = {'data_inicio' : data_inicio, 'data_fim' : data_fim }
        for key, value in params.items():
            if not value: raise ValueError(key)

        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def listar_despesas(self):
        return DespesaRepository().listar_despesas_do_periodo(self.data_inicio, self.data_fim)

    def calcular_saldo(self):
        despesas = DespesaRepository().listar_despesas_do_periodo(self.data_inicio, self.data_fim) 
        return sum(d.valor for d in despesas)

    def nome_do_mes(self):
        meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março', 4 : 'Abril', 
                 5 : 'Maio', 6 : 'Junho', 7 : 'Julho', 8 : 'Agosto', 
                 9 : 'Setembro', 10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro' }
        
        return meses[self.data_inicio.month]

    def obter_sumario(self):
        grupo = GrupoFiscal( (self.data_inicio, self.data_fim) )
        devedor = grupo.obter_devedor()
        
        autores = { autor : '%.2f' % valor for autor, valor in grupo.obter_autores().items() }

        sumario = { 'nome' : self.nome_do_mes(),
                    'total' : '%.2f' % self.calcular_saldo(),
                    'devedor' : devedor if devedor else '-',
                    'valor_divida' : '%.2f' % grupo.calcular_divida(devedor) }

        sumario.update(autores)

        return sumario
