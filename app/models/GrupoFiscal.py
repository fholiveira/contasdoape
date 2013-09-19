from .Despesa import Despesa 
from datetime import datetime

class GrupoFiscal():
    def __init__(self, periodo):
        if not periodo or not isinstance(periodo, tuple):
            raise ValueError('periodo')

        self._autores = self._carregar_autores(periodo)

    def _carregar_autores(self, periodo):
        data_inicio, data_fim = periodo            

        nomes = Despesa.objects(data__gte = data_inicio, 
                                data__lte = data_fim).distinct('nome')

        pessoas = { }
        for nome in nomes:
            pessoas[nome] = Despesa.objects(data__gte = data_inicio, 
                                            data__lte = data_fim,
                                            nome = nome).sum('valor')
        
        return pessoas
        
    def obter_devedor(self):
        return min(self._autores, key=self._autores.get) if self._autores else None

    def calcular_divida(self, autor):
        valor_por_autor = sum(self._autores.values()) / len(self._autores)
        return self._autores[autor] - valor_por_autor

    def obter_autores(self):
        return self._autores
