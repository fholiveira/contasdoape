from contasdoape.models.Despesa import Despesa
from contasdoape.models.Usuario import Usuario
from unittest import TestCase
from datetime import datetime

class TestDespesa(TestCase):

    def setUp(self):
        self.despesa = Despesa(Usuario(1, 'José'), 10.50, datetime.now())
    
    def test_deve_conter_descricao(self):
        self.assertTrue(hasattr(self.despesa, 'descricao'))

    def test_deve_conter_valor(self):
        self.assertTrue(hasattr(self.despesa, 'valor'))

    def test_deve_conter_id(self):
        self.assertTrue(hasattr(self.despesa, 'id'))

    def test_deve_conter_data(self):
        self.assertTrue(hasattr(self.despesa, "data"))

    def test_nao_deve_existir_sem_valor_positivo(self):
        with self.assertRaises(ValueError) as error:
            Despesa(Usuario(1, 'José'), -1, datetime.now())

        self.assertEqual('valor', str(error.exception))

    def test_nao_deve_existir_sem_data(self):
        with self.assertRaises(ValueError) as error:
            Despesa(Usuario(1, 'José'), 10.50, None)

        self.assertEqual('data', str(error.exception))
