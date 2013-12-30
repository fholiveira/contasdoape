from contasdoape.models.Usuario import Usuario

class ControleDeAcesso():
    def obter_usuario(self, facebook_id, nome):
        usuario = Usuario.objects(facebook_id = facebook_id).first()

        if not usuario:
            usuario = Usuario(facebook_id, nome)
        
        usuario.save()
        return usuario

    def carregar_usuario(self, id):
        return Usuario.objects(facebook_id = id).first()
