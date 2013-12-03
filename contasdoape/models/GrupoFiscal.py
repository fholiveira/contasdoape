from .DespesasRepository import DespesaRepository
from datetime import datetime
from .Despesa import Despesa 

class GrupoFiscal():
    def __init__(self, periodo):
        if not periodo:
            raise ValueError('periodo')

        self._autores = self._carregar_autores(periodo)

    def _carregar_autores(self, periodo):
        data_inicio, data_fim = periodo            

        despesas = DespesaRepository().listar_despesas_do_periodo(data_inicio, data_fim)
        nomes = list(set(d.nome for d in despesas))

        return { nome : sum(d.valor for d in despesas if d.nome == nome) for nome in nomes }
        
    def obter_devedor(self):
        return min(self._autores, key=self._autores.get) if self._autores else None

    def calcular_divida(self, autor):
        if len(self._autores) > 0:
            valor_por_autor = sum(self._autores.values()) / len(self._autores)
            return self._autores[autor] - valor_por_autor
        else:
            return 0

    def obter_autores(self):
        return self._autores
