from unittest import TestCase
from mongoengine import connect
from contasdoape.models.Ape import Ape
from contasdoape.models.Condominio import Condominio
from contasdoape.models.ControleDeAcesso import ControleDeAcesso

class TestApe(TestCase):
   
    @classmethod
    def setUpClass(cls):
        cls.conexao = connect('contasdoape-test')
        cls.usuario = ControleDeAcesso().obter_usuario('123456', 'João')

    def setUp(self):
        Ape.objects.delete()

    def test_deve_criar_apartamento(self):
        Condominio(self.usuario).criar_ape()
        ape = Ape.objects().first()
        
        self.assertIsNotNone(ape)

    def test_deve_obter_ape(self):
        novo_ape = Condominio(self.usuario).criar_ape()
        ape = Condominio(self.usuario).obter_ape()

        self.assertEquals(novo_ape.id, ape.id)
    
    def test_deve_associar_usuario_ao_criar_o_ape(self):
        Condominio(self.usuario).criar_ape()
        ape = Ape.objects().first()
        
        self.assertEquals(self.usuario.id, ape.membros[0].id)


    def test_deve_convidar_amigos(self):
        ape = Condominio(self.usuario).criar_ape()
        convidados = [ '111111', '222222' ]

        ape.adicionar_convidados(convidados)

        ape_salvo = Ape.objects.first()
        self.assertListEqual(ape_salvo.convidados, convidados)

    @classmethod
    def tearDownClass(cls):
       cls.conexao.drop_database('contasdoape-test')
