from contasdoape.models import Ape, Condominio, ControleDeAcesso
from mongoengine import connect
from unittest import TestCase


class TestApe(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conexao = connect('contasdoape-test')
        cls.usuario = ControleDeAcesso().obter_usuario('123456', 'João')

    def setUp(self):
        Ape.objects.delete()

    def test_deve_convidar_amigos(self):
        ape = Condominio(self.usuario).criar_ape()
        convidados = ['111111', '222222']

        ape.adicionar_convidados(convidados)

        ape_salvo = Ape.objects.first()
        self.assertListEqual(ape_salvo.convidados, convidados)

    @classmethod
    def tearDownClass(cls):
        cls.conexao.drop_database('contasdoape-test')
