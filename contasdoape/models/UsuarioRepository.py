from .Usuario import Usuario

class UsuarioRepository():
    def carregar_ou_criar(self, facebook_id, username, nome):
        usuario = Usuario.objects(facebook_id = facebook_id).first()

        if not usuario:
            usuario = Usuario(facebook_id, username, nome)
            usuario.save()

        return usuario

    def carregar(id):
        return Usuario.objects(facebook_id = id).first()
