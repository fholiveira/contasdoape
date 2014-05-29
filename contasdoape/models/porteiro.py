from . import Ape, Convite, Usuario


class Porteiro:
    def __init__(self, usuario):
        self.usuario = usuario

    def tem_ape(self):
        return Ape.objects(membros__contains=self.usuario.id)

    def eh_convidado(self):
        fb_id = self.usuario.facebook_id
        return Ape.objects(convites__destinatario__contains=fb_id)

    @staticmethod
    def obter_usuario(facebook_id, nome):
        usuario = Usuario.objects(facebook_id=facebook_id).first()

        if not usuario:
            usuario = Usuario(facebook_id, nome)
            usuario.save()

        return usuario

    @staticmethod
    def carregar_usuario(fb_id):
        return Usuario.objects(facebook_id=fb_id).first()
