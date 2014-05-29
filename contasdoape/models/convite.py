from mongoengine import (EmbeddedDocument, StringField, ReferenceField,
                         DateTimeField)
from datetime import datetime
from . import Usuario


class Convite(EmbeddedDocument):
    remetente = ReferenceField(Usuario)
    destinatario = StringField(required=True)
    data = DateTimeField(required=True)

    def __init__(self, remetente, destinatario, *args, **kwargs):
        EmbeddedDocument.__init__(self, *args, **kwargs)

        if not destinatario:
            raise ValueError('destinatario')

        self.data = datetime.now()
        self.remetente = remetente
        self.destinatario = destinatario
