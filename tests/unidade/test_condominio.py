from contasdoape.models import Condominio, Usuario, Ape
from unittest.mock import patch
from unittest import TestCase


class TestCondominio(TestCase):

    def test_deve_adicionar_usuario_como_membro_do_ape_criado(self):
        usuario = Usuario(1, 'joão')
        with patch('contasdoape.models.Ape.save') as objeto:
            ape = Condominio(usuario).criar_ape()
            self.assertIn(usuario, ape.membros)

    def deve_incluir_usuario_como_membro_ao_aceitar_o_convite(self):
        usuario = Usuario(1, 'joão')
        with patch('contasdoape.models.Ape.save') as objeto:
            metodo = 'contasdoape.models.ControleDeAcesso.carregar_usuario'
            with patch(metodo) as objeto2:
                objeto2.return_value = usuario
                ape = Condominio(usuario).aceitar_convite()
                self.assertIn(usuario, ape.membros)

    def deve_excluir_usuario_da_lista_de_convidados_ao_aceitar_o_convite(self):
        usuario = Usuario(1, 'joão')
        with patch('contasdoape.models.Ape.save') as objeto:
            ape = Condominio(usuario).aceitar_convite()
            self.assertNotIn(usuario.facebook_id, ape.convidados)
