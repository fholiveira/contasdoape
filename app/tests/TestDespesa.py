from unittest import TestCase
from models.Despesa import Despesa
from datetime import datetime

class TestDespesa(TestCase):

    def setUp(self):
        self.despesa = Despesa(valor = 1, nome = "Ususario", data = datetime.now)
    
    def test_deve_conter_descricao(self):
        self.assertTrue(hasattr(self.despesa, "descricao"))

    def test_deve_conter_nome(self):
        self.assertTrue(hasattr(self.despesa, "nome"))

    def test_deve_conter_valor(self):
        self.assertTrue(hasattr(self.despesa, "valor"))

    def test_deve_conter_data(self):
        self.assertTrue(hasattr(self.despesa, "data"))

    def test_nao_deve_existir_sem_valor_positivo(self):
        self.assertRaises(ValueError, Despesa(valor = 0))

    def test_nao_deve_existir_sem_nome(self):
        self.assertRaises(ValueError, Despesa(valor = 2, nome = None))
