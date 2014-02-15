from mongoengine import Document, StringField, DateTimeField
from mongoengine import ReferenceField, ListField, EmbeddedDocumentField
from contasdoape.models.Usuario import Usuario
from contasdoape.models.Despesa import Despesa
from bson.objectid import ObjectId
from datetime import datetime

class Ape(Document):
    nome = StringField()
    convidados = ListField(StringField())
    membros = ListField(ReferenceField(Usuario))
    data_criacao = DateTimeField(required = True)
    despesas = ListField(EmbeddedDocumentField(Despesa))
    
    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        self.data_criacao = datetime.now()

    def incluir_despesa(self, despesa):
        despesa.id = ObjectId()
        self.despesas.append(despesa)
        self.save()

    def adicionar_convidados(self, ids_convidados):
        ids = [fb_id for fb_id in ids_convidados if fb_id]
        self.convidados.extend(ids)
        self.save()
    
    def remover_despesa(self, despesa):
        self.despesas.remove(despesa)
        self.save()
