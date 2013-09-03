from unittest import TestCase
from models.Despesa import Despesa

class TestDespesa(TestCase):

    def setUp(self):
        self.despesa = Despesa()
    
    def test_deve_conter_descricao(self):
        self.assertTrue(hasattr(self.despesa, "descricao"))

    def test_deve_conter_nome(self):
        self.assertTrue(hasattr(self.despesa, "nome"))

    def test_deve_conter_valor(self):
        self.assertTrue(hasattr(self.despesa, "valor"))

    def test_deve_conter_data(self):
        self.assertTrue(hasattr(self.despesa, "data"))
