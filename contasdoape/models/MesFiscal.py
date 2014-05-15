from contasdoape.models.Despesa import Despesa
from datetime import datetime
from itertools import groupby


class MesFiscal():
    def __init__(self, ape, data_inicio, data_fim):
        params = {'data_inicio': data_inicio,
                  'data_fim': data_fim,
                  'ape': ape}

        for key, value in params.items():
            if not value:
                raise ValueError(key)

        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.ape = ape
        
    def numero(self):
        data = self.data_fim if self.data_fim.day >= 15 else self.data_inicio
        return (data.month, data.year)

    def listar_despesas(self):
        despesas = [despesa for despesa in self.ape.despesas
                    if despesa.data >= self.data_inicio and
                    despesa.data <= self.data_fim]

        return sorted(despesas, key=lambda despesa: despesa.data)

    def remover_despesa(self, usuario, id_despesa):
        despesa = next(d for d in self.ape.despesas if str(d.id) == id_despesa)

        if usuario.id != despesa.autor.id:
            raise Exception('Um usuário só pode excluir despesas que ele mesmo criou.')

        self.ape.remover_despesa(despesa)

    def calcular_saldo(self):
        despesas = self.listar_despesas()
        return sum(d.valor for d in despesas)

    def nome_do_mes(self):
        meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
                 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
                 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

        mes, _ = self.numero()
        return meses[mes]

    def obter_despesas(self, autor=None):
        lista_despesas = self.listar_despesas()
        despesas_por_autor = {} 
        for membro in self.ape.membros:
            despesas_por_autor[membro] = [d for d in lista_despesas if d.autor == membro]    

        if autor:
            return next(list(despesas) for usuario, despesas in despesas_por_autor.items()
                        if usuario.id == autor.id)

        return despesas_por_autor
