from contasdoape.models.Ape import Ape

class Condominio:
    def obter_ape(self, usuario):
        return Ape.objects(membros__contains = usuario).first()

    def criar_ape(self, usuario):
        ape = Ape()
        ape.membros.append(usuario)
        ape.save()

        return ape
    
    def tem_ape(self, usuario):
        return self.obter_ape(usuario) is not None
