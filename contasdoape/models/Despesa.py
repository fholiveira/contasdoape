from mongoengine import Document, EmbeddedDocument, StringField
from mongoengine import ReferenceField, FloatField, DateTimeField
from contasdoape.models.Usuario import Usuario
from datetime import datetime

class Despesa(EmbeddedDocument):
    autor = ReferenceField(Usuario)
    valor = FloatField(required = True)
    data = DateTimeField(required = True)
    descricao = StringField()

    def __init__(self, autor, valor, data, *args, **kwargs):
        EmbeddedDocument.__init__(self)
      
        params = {'valor' : valor, 'autor' : autor, 'data' : data}
        for key, value in params.items():
            if not value: raise ValueError(key)
            
        if valor <= 0: 
            raise ValueError('valor')
        
        self.autor = autor
        self.valor = valor
        self.data = data

    def to_dict(self):
        return  {'valor' : 'R$ ' + str(self.valor), 
                 'data' : self.data.strftime('%d/%m/%Y'), 
                 'autor' : self.autor.nome,
                 'descricao' : self.descricao,
                 'id' : self.id }
