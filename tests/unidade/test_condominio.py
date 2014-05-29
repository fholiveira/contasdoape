from contasdoape.models import Condominio, Usuario, Ape, Convite
from bson.objectid import ObjectId
from unittest.mock import patch
from unittest import TestCase


class TestCondominio(TestCase):
    def setUp(self):
        self.membro = Usuario('1111', 'João', id=ObjectId())
        self.convidado = Usuario('2222', 'José', id=ObjectId())

        self.ape = Ape()
        self.ape.membros = [self.membro]
        self.ape.convites = [Convite(self.membro, '2222')]
        self.ape.save = lambda: None

    def test_deve_adicionar_usuario_como_membro_do_ape_criado(self):
        usuario = Usuario('1111', 'João')
        condominio = Condominio(usuario)
        condominio.porteiro.tem_ape = lambda: False

        with patch('contasdoape.models.Ape.save') as method:
            ape = condominio.criar_ape()

        self.assertIn(usuario, ape.membros)

    def test_deve_incluir_usuario_como_membro_ao_aceitar_o_convite(self):
        condominio = Condominio(self.convidado)
        condominio.obter_ape = lambda: self.ape

        condominio.aceitar_convite()

        self.assertIn(self.convidado, self.ape.membros)

    def test_deve_excluir_usuario_dos_convites_ao_aceitar_o_convite(self):
        condominio = Condominio(self.convidado)
        condominio.obter_ape = lambda: self.ape

        condominio.aceitar_convite()

        self.assertNotIn(self.convidado.facebook_id,
                         [c.destinatario for c in self.ape.convites])

    def test_deve_ignorar_ids_vazios_ao_montar_a_lista_de_convidados(self):
        condominio = Condominio(self.membro)
        condominio.obter_ape = lambda: self.ape

        condominio.incluir_convidados(['9999', '', '9999'])

        self.assertNotIn('',
                         [c.destinatario for c in self.ape.convites])

    def test_nao_deve_permitir_que_convidados_incluam_convidados(self):
        condominio = Condominio(self.convidado)
        condominio.obter_ape = lambda: self.ape

        with self.assertRaises(Exception) as error:
            condominio.incluir_convidados(['9999', '8888'])

    def test_somente_convidados_podem_aceitar_convite(self):
        condominio = Condominio(self.membro)
        condominio.obter_ape = lambda: self.ape

        with self.assertRaises(Exception) as error:
            condominio.aceitar_convite()

    def test_nao_pode_criar_ape_se_ja_tem_ape(self):
        condominio = Condominio(self.membro)
        condominio.porteiro.tem_ape = lambda x: True

        with self.assertRaises(Exception) as error:
            condominio.criar_ape()
