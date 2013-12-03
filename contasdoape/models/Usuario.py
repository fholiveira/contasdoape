from mongoengine import StringField

class Usuario(Document):
    nome = StringField(required = True)
    facebook_id = StringField(required = True)
    
    def __init__(self, nome, facebook_id):
        self.nome = nome
        self.facebook_id = facebook_id

    def __repr__(self):
        return '<User %r>' % self.nome
