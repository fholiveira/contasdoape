from mongoengine import ReferenceField, ListField, EmbeddedDocumentField
from mongoengine import Document, StringField, DateTimeField, IntField
from . import Usuario, Despesa
from bson.objectid import ObjectId
from datetime import datetime


class Ape(Document):
    nome = StringField()
    convidados = ListField(StringField())
    membros = ListField(ReferenceField(Usuario))
    data_criacao = DateTimeField(required=True)
    despesas = ListField(EmbeddedDocumentField(Despesa))
    dia_do_acerto = IntField(required=True, default=1)

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        self.data_criacao = datetime.now()

    def incluir_despesa(self, despesa):
        despesa.id = ObjectId()
        self.despesas.append(despesa)
        self.save()

    def adicionar_convidados(self, ids_convidados):
        blacklist = self.convidados + [m.facebook_id for m in self.membros]

        ids = [fb_id for fb_id in ids_convidados
               if fb_id and fb_id not in blacklist]

        self.convidados.extend(ids)
        self.save()

    def remover_despesa(self, despesa):
        self.despesas.remove(despesa)
        self.save()
