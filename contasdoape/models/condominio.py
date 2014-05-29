from . import Ape, Convite, Porteiro


class Condominio:
    def __init__(self, usuario):
        self.usuario = usuario
        self.porteiro = Porteiro(usuario)

    def obter_ape(self):
        if self.porteiro.tem_ape():
            return Ape.objects(membros__contains=self.usuario.id).first()
        elif self.porteiro.eh_convidado(self.usuario):
            fb_id = self.usuario.facebook_id
            return Ape.objects(convidados__contains=fb_id).first()

    def criar_ape(self):
        if self.porteiro.tem_ape():
            raise Exception('Você não pode ter mais de um apê.')

        ape = Ape()
        ape.membros.append(self.usuario)
        ape.save()

        return ape

    def incluir_convidados(self, ids):
        ape = self.obter_ape()

        if self.usuario.id not in [membro.id for membro in ape.membros]:
            raise Exception('Somente membros podem convidar pessoas')

        convites = [Convite(self.usuario, fb_id) for fb_id in ids if fb_id]
        ape.adicionar_convites(convites)

    def aceitar_convite(self):
        ape = self.obter_ape()

        if self.usuario.facebook_id not in [convite.destinatario
                                            for convite in ape.convites]:
            raise Exception('Somente convidados podem entrar no apê.')

        ape.membros.append(self.usuario)
        ape.convites = [c for c in ape.convites
                        if c.destinatario != self.usuario.facebook_id]
        ape.save()
