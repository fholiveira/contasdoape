from . import Usuario


class ControleDeAcesso():
    def obter_usuario(self, facebook_id, nome):
        usuario = Usuario.objects(facebook_id=facebook_id).first()

        if not usuario:
            usuario = Usuario(facebook_id, nome)
            usuario.save()

        return usuario

    def carregar_usuario(self, fb_id):
        return Usuario.objects(facebook_id=fb_id).first()
