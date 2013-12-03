from mongoengine import Document, StringField, FloatField, DateTimeField
from datetime import datetime

class Despesa(Document):
    nome = StringField(required = True)
    descricao = StringField(required = False)
    valor = FloatField(required = True)
    data = DateTimeField(required = True)

    def __init__(self, valor, nome, data, *args, **kwargs):
        Document.__init__(self, args, kwargs)
      
        params = {'valor' : valor, 'nome' : nome, 'data' : data}
        for key, value in params.items():
            if not value: raise ValueError(key)
        
        self.nome = nome
        self.valor = valor
        self.data = data

    def to_dict(self):
        return  {'valor' : 'R$ ' + str(self.valor), 
                 'data' : self.data.strftime('%d/%m/%Y'), 
                 'autor' : self.nome,
                 'descricao' : self.descricao,
                 'id' : self.id }
