from mongoengine import Document, StringField, ReferenceField, ObjectIdField


class Usuario(Document):
    nome = StringField(required=True)
    facebook_id = StringField(required=True)

    def __init__(self, facebook_id, nome, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)

        if not nome:
            raise ValueError('nome')

        if not facebook_id:
            raise ValueError('facebook_id')

        self.nome = nome
        self.facebook_id = facebook_id

    def get_image_url(self):
        return 'https://graph.facebook.com/' + self.facebook_id + '/picture'

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
