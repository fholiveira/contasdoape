from contasdoape.models import Despesa, Usuario, Ape, Convite
from unittest.mock import patch, Mock
from unittest import TestCase
from datetime import datetime


class TestApe(TestCase):

    def setUp(self):
        self.ape = Ape()
        self.ape.membros = [Usuario('1234', 'João'),
                            Usuario('2345', 'José'),
                            Usuario('3456', 'Will')]
        self.ape.convites = [Convite(Usuario('1234', 'João'), '9999'),
                             Convite(Usuario('2345', 'José'), '8888'),
                             Convite(Usuario('3456', 'Will'), '7777')]
        self.ape.save = lambda: None

    def test_deve_definir_id_para_a_depesa_ao_inclui_la(self):
        despesa = Despesa(Usuario('1234', 'João'), 35, datetime.now())
        self.ape.incluir_despesa(despesa)
        self.assertIsNotNone(despesa.id)

    def test_deve_incluir_despesa(self):
        despesa = Despesa(Usuario('1234', 'João'), 35, datetime.now())
        self.ape.incluir_despesa(despesa)
        self.assertIn(despesa, self.ape.despesas)

    def test_deve_excluir_despesa(self):
        despesa = Despesa(Usuario('1234', 'João'), 35, datetime.now())
        self.ape.despesas.append(despesa)
        self.ape.remover_despesa(despesa)
        self.assertNotIn(despesa, self.ape.despesas)

    def test_nao_deve_incluir_convidados_nulos(self):
        convites = [Convite(Usuario('1234', 'João'), '1111'),
                    Convite(Usuario('2345', 'José'), '7777'),
                    Convite(Usuario('3456', 'Will'), '2222')]

        self.ape.adicionar_convites(convites)

        self.assertNotIn(None, [c.destinatario for c in self.ape.convites])

    def test_nao_deve_duplicar_convidados(self):
        convites = [Convite(Usuario('1234', 'João'), '1111'),
                    Convite(Usuario('2345', 'José'), '7777'),
                    Convite(Usuario('3456', 'Will'), '2222')]

        self.ape.adicionar_convites(convites)

        self.assertCountEqual(['1111', '2222', '7777', '8888', '9999'],
                              [c.destinatario for c in self.ape.convites])

    def test_nao_deve_adicionar_como_convidados_os_membros_do_ape(self):
        convites = [Convite(Usuario('1234', 'João'), '1111'),
                    Convite(Usuario('2345', 'José'), '1234'),
                    Convite(Usuario('3456', 'Will'), '2222')]

        self.ape.adicionar_convites(convites)

        self.assertCountEqual(['1111', '2222', '7777', '8888', '9999'],
                              [c.destinatario for c in self.ape.convites])

    def test_deve_adicionar_convidados(self):
        ids = ['111', '222']
        convites = [Convite(Usuario('1234', 'João'), '1111'),
                    Convite(Usuario('3456', 'Will'), '2222')]

        self.ape.adicionar_convites(convites)

        self.assertCountEqual(['1111', '2222', '7777', '8888', '9999'],
                              [c.destinatario for c in self.ape.convites])
