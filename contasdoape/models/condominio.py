from contasdoape.models import ControleDeAcesso, Ape


class Condominio:
    def __init__(self, usuario):
        self.usuario = usuario

    def tem_ape(self):
        return Ape.objects(membros__contains=self.usuario.id)

    def eh_convidado(self):
        return Ape.objects(convidados__contains=self.usuario.facebook_id)

    def obter_ape(self):
        if self.tem_ape():
            return Ape.objects(membros__contains=self.usuario.id).first()
        elif self.eh_convidado():
            return Ape.objects(convidados__contains=self.usuario.facebook_id).first()

    def criar_ape(self):
        ape = Ape()
        ape.membros.append(self.usuario)
        ape.save()

        return ape

    def aceitar_convite(self):
        ape = self.obter_ape()

        ape.membros.append(ControleDeAcesso().carregar_usuario(self.usuario.facebook_id))

        ape.convidados.remove(self.usuario.facebook_id)
        ape.save()
