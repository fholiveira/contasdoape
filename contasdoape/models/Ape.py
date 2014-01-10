from mongoengine import Document, StringField, DateTimeField
from mongoengine import ReferenceField, ListField, EmbeddedDocumentField
from contasdoape.models.Usuario import Usuario
from contasdoape.models.Despesa import Despesa
from datetime import datetime

class Ape(Document):
    nome = StringField()
    membros = ListField(ReferenceField(Usuario))
    data_criacao = DateTimeField(required = True)
    despesas = ListField(EmbeddedDocumentField(Despesa))
    
    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        self.data_criacao = datetime.now()

    def incluir_despesa(self, despesa):
        self.despesas.append(despesa)
        self.save()
