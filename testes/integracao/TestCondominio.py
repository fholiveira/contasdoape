from contasdoape.models.Condominio import Condominio
from contasdoape.models.Usuario import Usuario
from contasdoape.models.Ape import Ape
from mongoengine import connect
from unittest import TestCase


class TestCondominio(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conexao = connect('contasdoape-test')

    def setUp(self):
        Ape.objects.delete()
        Usuario.objects.delete()

        self.usuario = Usuario('1234', 'Pedro')
        self.usuario.save()

    def test_deve_confirmar_que_um_usuario_tem_ape(self):
        ape = Ape()
        ape.membros.append(self.usuario)
        ape.save()

        self.assertTrue(Condominio(self.usuario).tem_ape())

    def test_deve_confirmar_que_um_usuario_eh_convidado(self):
        ape = Ape()
        ape.convidados.append('1234')
        ape.save()

        self.assertTrue(Condominio(self.usuario).eh_convidado())

    def test_deve_obter_o_ape_de_um_convidado(self):
        ape = Ape()
        ape.convidados.append('1234')
        ape.save()

        self.assertEquals(ape, Condominio(self.usuario).obter_ape())

    def test_deve_obter_o_ape_de_um_membro(self):
        ape = Ape()
        ape.membros.append(self.usuario)
        ape.save()

        self.assertEquals(ape, Condominio(self.usuario).obter_ape())

    def test_deve_criar_ape(self):
        Condominio(self.usuario).criar_ape()

        self.assertEquals(1, len(Ape.objects().all()))

    def test_deve_adicionar_usuario_como_membro_ao_criar_ape_para_ele(self):
        Condominio(self.usuario).criar_ape()

        self.assertIn(self.usuario, Ape.objects().first().membros)

    def test_deve_incluir_usuario_como_membro_ao_aceitar_o_convite(self):
        ape = Ape()
        ape.convidados.append('1234')
        ape.save()

        Condominio(self.usuario).aceitar_convite()

        self.assertIn(self.usuario, Ape.objects().first().membros)

    def test_deve_remover_usuario_da_lista_de_convidados_ao_aceitar_o_convite(self):
        ape = Ape()
        ape.convidados.append('1234')
        ape.save()

        Condominio(self.usuario).aceitar_convite()

        self.assertNotIn(self.usuario.facebook_id, Ape.objects().first().convidados)

    @classmethod
    def tearDownClass(cls):
        cls.conexao.drop_database('contasdoape-test')
