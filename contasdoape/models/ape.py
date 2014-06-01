from mongoengine import (ReferenceField, ListField, EmbeddedDocumentField,
                         Document, StringField, DateTimeField, IntField)
from . import Usuario, Despesa, Convite
from bson.objectid import ObjectId
from datetime import datetime


class Ape(Document):
    nome = StringField()
    convidados = ListField(StringField())
    data_criacao = DateTimeField(required=True)
    membros = ListField(ReferenceField(Usuario))
    convites = ListField(EmbeddedDocumentField(Convite))
    despesas = ListField(EmbeddedDocumentField(Despesa))
    dia_do_acerto = IntField(required=True, default=1)

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        self.data_criacao = datetime.now()

    def incluir_despesa(self, despesa):
        despesa.id = ObjectId()
        self.despesas.append(despesa)
        self.save()

    def adicionar_convites(self, convites):
        blacklist = [convite.destinatario for convite in self.convites] + \
                    [membro.facebook_id for membro in self.membros]

        convites_validos = [convite for convite in convites
                            if convite and
                            convite.destinatario not in blacklist]

        self.convites.extend(convites_validos)
        self.save()

    def remover_despesa(self, despesa):
        self.despesas.remove(despesa)
        self.save()
