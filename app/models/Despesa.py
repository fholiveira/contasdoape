from mongoengine import Document, StringField, FloatField, DateTimeField

class Despesa(Document):
    nome = StringField(required = True)
    descricao = StringField(required = True)
    valor = FloatField(required = True)
    data = DateTimeField(required = True)
