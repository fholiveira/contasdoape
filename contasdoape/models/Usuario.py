from mongoengine import Document, StringField

class Usuario(Document):
    nome = StringField(required = True)
    username = StringField(required = True)
    facebook_id = StringField(required = True)
    ape = ReferenceField()
    
    def __init__(self, facebook_id, username, nome,  *args, **kwargs):
        Document.__init__(self, args, kwargs)
        self.nome = nome
        self.username = username
        self.facebook_id = facebook_id
    
    def obter_despesas(self, data_inicio, data_fim):
        if not ape: return []

        return [despesa in ape.despesas 
                    if despesa.data >= data_inicio and
                       despesa.data <= data_fim]

    def get_image_url(self):
        return 'https://graph.facebook.com/' + self.username + '/picture'

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
