from unittest import TestCase
from models.Despesa import Despesa
from datetime import datetime

class TestDespesa(TestCase):

    def setUp(self):
        self.despesa = Despesa(valor = 1, nome = "Ususario", data = datetime.now())
    
    def test_deve_conter_descricao(self):
        self.assertTrue(hasattr(self.despesa, "descricao"))

    def test_deve_conter_nome(self):
        self.assertTrue(hasattr(self.despesa, "nome"))

    def test_deve_conter_valor(self):
        self.assertTrue(hasattr(self.despesa, "valor"))

    def test_deve_conter_data(self):
        self.assertTrue(hasattr(self.despesa, "data"))

    def test_nao_deve_existir_sem_valor_positivo(self):
        with self.assertRaises(ValueError) as error:
            Despesa(valor = 0, nome = 'Teste', data = datetime.now())

        self.assertEqual("valor", str(error.exception))

    def test_nao_deve_existir_sem_nome(self):
        with self.assertRaises(ValueError) as error:
            Despesa(valor = 1, nome = None, data = datetime.now())

        self.assertEqual("nome", str(error.exception))
    
    def test_nao_deve_existir_sem_data(self):
        with self.assertRaises(ValueError) as error:
            Despesa(valor = 1, nome = "Teste", data = None)

        self.assertEqual("data", str(error.exception))
