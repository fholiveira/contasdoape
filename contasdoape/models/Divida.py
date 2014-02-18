class Divida():
    def __init__(self, gastos_por_pessoa, usuario):
        self.usuario = usuario
        self.gastos = { pessoa : sum(d.valor for d in despesas)
                        for pessoa, despesas in gastos_por_pessoa.items() }
    
    def valor_total(self):
        return sum(gasto for pessoa, gasto in self.gastos.items())

    def valor_gasto(self):
        return next((g for p, g in self.gastos.items() if p.id == self.usuario.id), 0) 
        
    def valor_medio(self):
        return self.valor_total() / len(self.gastos)

    def divida_relativa(self):
        custos = self.valor_gasto()
        media = self.valor_medio()

        if custos == media: 
            return {}
        
        ha_divida = self._ah_divida(custos, media)
        return { pessoa : gastos for pessoa, gastos in self.gastos.items() if ha_divida(gastos) }

    def _ah_divida(self, custos, media): 
        if custos > media:
            return lambda gastos: gastos < media
        
        return lambda gastos: gastos > media
