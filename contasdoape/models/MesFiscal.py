from contasdoape.models.Despesa import Despesa 
from datetime import datetime
from itertools import groupby

class MesFiscal():
    def __init__(self, ape, data_inicio, data_fim):
        params = {'data_inicio' : data_inicio, 
                  'data_fim' : data_fim, 
                  'ape' : ape}

        for key, value in params.items():
            if not value: raise ValueError(key)

        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.ape = ape

    def listar_despesas(self):
        return [despesa for despesa in self.ape.despesas
                    if despesa.data >= self.data_inicio and 
                       despesa.data <= self.data_fim]

    def remover_despesa(self, usuario, id_despesa):
        despesa = next(d for d in self.ape.despesas if str(d.id) == id_despesa)
        
        if usuario.id != despesa.autor.id:
            raise Exception('Um usuário só pode excluir despesas que ele mesmo criou.')

        self.ape.remover_despesa(despesa)

    def calcular_saldo(self):
        despesas = self.listar_despesas()
        return sum(d.valor for d in despesas)

    def nome_do_mes(self):
        meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março', 4 : 'Abril', 
                 5 : 'Maio', 6 : 'Junho', 7 : 'Julho', 8 : 'Agosto', 
                 9 : 'Setembro', 10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro' }
        
        return meses[self.data_inicio.month]

    def obter_despesas(self, autor=None):
        despesas_por_autor = groupby(self.listar_despesas(), lambda d : d.autor)

        if autor:
            return next(list(despesas) for usuario, despesas in despesas_por_autor
                        if usuario.id == autor.id )

        return { autor : list(despesas) for autor, despesas in despesas_por_autor }
