from contasdoape.models import Porteiro, Usuario
from mongoengine import connect
from unittest import TestCase


class TestPorteiro(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conexao = connect('contasdoape-test')

    def setUp(self):
        Usuario.objects().delete()

    def test_deve_carregar_usuario_previamente_salvo(self):
        usuario = Usuario('12345678', 'Walter Kovacs')
        usuario.save()

        self.assertEquals(usuario,
                          Porteiro.carregar_usuario('12345678'))

    def test_deve_obter_por_nome_e_id_usuario_previamente_salvo(self):
        usuario = Usuario('12345678', 'Walter Kovacs')
        usuario.save()

        obtido = Porteiro.obter_usuario('12345678', 'Walter Kovacs')
        self.assertEquals(usuario, obtido)

    def test_deve_criar_usuario_ao_tentar_obter_um_usuario_inexistente(self):
        usuario = Porteiro.obter_usuario('12345678', 'Walter Kovacs')
        self.assertEquals(usuario, Usuario.objects().first())

    @classmethod
    def tearDownClass(cls):
        cls.conexao.drop_database('contasdoape-test')
