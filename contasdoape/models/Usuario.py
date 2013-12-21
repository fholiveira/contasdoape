from mongoengine import Document, StringField

class Usuario(Document):
    nome = StringField(required = True)
    facebook_id = StringField(required = True)
    
    def __init__(self, nome, facebook_id, *args, **kwargs):
        Document.__init__(self, args, kwargs)
        self.nome = nome
        self.facebook_id = facebook_id
    
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.facebook_id)

    def __repr__(self):
        return '<User %r>' % self.nome
