from unittest import TestCase
from mongoengine import connect
from contasdoape.models.Ape import Ape
from contasdoape.models.Condominio import Condominio
from contasdoape.models.ControleDeAcesso import ControleDeAcesso

class TestApe(TestCase):
    def setUp(self):
        self.conexao = connect('contasdoape-test')
        self.usuario = ControleDeAcesso().obter_usuario('123456', 'João')

    def test_deve_criar_apartamento(self):
        Ape.objects.delete()
        
        Condominio().criar_ape(self.usuario)
        ape = Ape.objects().first()
        
        self.assertIsNotNone(ape)

    def test_deve_obter_ape(self):
        Ape.objects.delete()

        novo_ape = Condominio().criar_ape(self.usuario)
        ape = Condominio().obter_ape(self.usuario)

        self.assertEquals(novo_ape.id, ape.id)
    
    def test_deve_associar_usuario_ao_criar_o_ape(self):
        Ape.objects.delete()
        
        Condominio().criar_ape(self.usuario)
        ape = Ape.objects().first()
        
        self.assertEquals(self.usuario.id, ape.membros[0].id)

    def tearDown(self):
       self.conexao.drop_database('contasdoape-test')
