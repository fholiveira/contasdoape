from contasdoape.models.Despesa import Despesa
from contasdoape.models.Usuario import Usuario
from contasdoape.models.Ape import Ape
from unittest.mock import patch, Mock
from unittest import TestCase
from datetime import datetime

class TestApe(TestCase):
    def setUp(self):
        self.ape = Ape()
        self.ape.convidados = ['999', '888', '777']
        self.ape.save = lambda: None

    def test_deve_definir_id_para_a_depesa_ao_inclui_la(self):
        despesa = Despesa(Usuario(1, 'João'), 35, datetime.now())
        self.ape.incluir_despesa(despesa)
        self.assertIsNotNone(despesa.id)

    def test_deve_incluir_despesa(self):
        despesa = Despesa(Usuario(1, 'João'), 35, datetime.now())
        self.ape.incluir_despesa(despesa)
        self.assertIn(despesa, self.ape.despesas)

    def test_deve_excluir_despesa(self):
        despesa = Despesa(Usuario(1, 'João'), 35, datetime.now())
        self.ape.despesas.append(despesa)
        self.ape.remover_despesa(despesa)
        self.assertNotIn(despesa, self.ape.despesas)

    def test_nao_deve_incluir_convidados_nulos(self):
        ids = ['111', None, '222']
        self.ape.adicionar_convidados(ids)
        self.assertNotIn(None, self.ape.convidados)

    def test_nao_deve_duplicar_convidados(self):
        ids = ['111', '777', '222']
        self.ape.adicionar_convidados(ids)
        self.assertCountEqual(['111', '222', '777', '888', '999'], self.ape.convidados)

    def test_deve_adicionar_convidados(self):
        ids = ['111', '222']
        self.ape.adicionar_convidados(ids)
        self.assertCountEqual(['111', '222', '777', '888', '999'], self.ape.convidados)
