from .Usuario import Usuario

class UsuarioRepository():
    def carregar_ou_criar(self, nome, facebook_id):
        usuario = Usuario.objects(nome = nome, 
                                  facebook_id = facebook_id).first()

        if not usuario:
            usuario = Usuario(nome, facebook_id)
            usuario.save()

        return usuario

    def carregar(id):
        return Usuario.objects(facebook_id = id).first()
