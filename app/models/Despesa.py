from mongoengine import Document, StringField, FloatField, DateTimeField
from datetime import datetime

class Despesa(Document):
    nome = StringField(required = True)
    descricao = StringField(required = True)
    valor = FloatField(required = True)
    data = DateTimeField(required = True)

    def __init__(self, valor, nome, data, *args, **kwargs):
        Document.__init__(self, args, kwargs)
        self._validar_parametros_de_construcao(valor, nome, data)

        self.nome = nome
        self.valor = valor
        self.data = data

    def _validar_parametros_de_construcao(self, valor, nome, data):
        if not valor and not isinstance(valor, float):
            raise ValueError("valor")

        if not nome and not isinstance(nome, str):
            raise ValueError("nome")

        if not data and not isinstance(data, datetime):
            raise ValueError("data")

    def to_dict(self):
        return  {'valor' : 'R$ ' + str(self.valor), 
                 'data' : self.data.strftime('%d/%m/%Y'), 
                 'autor' : self.nome,
                 'descricao' : self.descricao,
                 'id' : self.id }
                
        
