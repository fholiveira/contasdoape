from unittest import TestCase
from models.MesFiscal import MesFiscal
from datetime import datetime

class TestDespesa(TestCase):

    def setUp(self):
        self.mes_fiscal = MesFiscal(datetime(2013,10,10), datetime(2013,11,10))
    
    def test_deve_conter_data_inicio(self):
        self.assertTrue(hasattr(self.mes_fiscal, "_data_inicio"))

    def test_deve_conter_data_fim(self):
        self.assertTrue(hasattr(self.mes_fiscal, "_data_fim"))

    def test_nao_deve_existir_sem_data_inicial_valida(self):
        with self.assertRaises(ValueError) as error:
            MesFiscal("Data inicial", datetime(2013, 11, 10))

        self.assertEqual("data_inicio", str(error.exception))

    def test_nao_deve_existir_sem_data_fim_valida(self):
        with self.assertRaises(ValueError) as error:
            MesFiscal(datetime(2013, 11, 10), "sasasdasf f")

        self.assertEqual("data_fim", str(error.exception))
