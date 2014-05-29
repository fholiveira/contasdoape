from contasdoape.models import Ape, Condominio, Convite, Porteiro
from mongoengine import connect
from unittest import TestCase


class TestApe(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conexao = connect('contasdoape-test')
        cls.usuario = Porteiro.obter_usuario('123456', 'João')

    def setUp(self):
        Ape.objects.delete()

    def test_deve_convidar_amigos(self):
        ape = Condominio(self.usuario).criar_ape()
        convites = [Convite(self.usuario, '111111'),
                    Convite(self.usuario, '222222')]

        ape.adicionar_convites(convites)

        ape_salvo = Ape.objects.first()
        self.assertListEqual([c.destinatario for c in ape_salvo.convites],
                             ['111111', '222222'])

    @classmethod
    def tearDownClass(cls):
        cls.conexao.drop_database('contasdoape-test')
