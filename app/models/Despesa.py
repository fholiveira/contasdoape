from mongoengine import Document, StringField, FloatField, DateTimeField

class Despesa(Document):
    nome = StringField(required = True)
    descricao = StringField(required = True)
    valor = FloatField(required = True)
    data = DateTimeField(required = True)

    def __init__(self, valor, nome, data):
        self._validar_parametros_de_construcao(valor, nome)

        self.nome = nome
        self.valor = valor
        
    def _validar_parametros_de_construcao(self, valor, nome):
        if not valor:
            raise ValueError("valor")

        if not nome:
            raise ValueError(nome)
