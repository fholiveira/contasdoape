from contasdoape.models.MesFiscal import MesFiscal
from contasdoape.models.Despesa import Despesa
from contasdoape.models.Usuario import Usuario
from contasdoape.models.Ape import Ape
from unittest.mock import patch
from unittest import TestCase
from datetime import datetime

class TestMesfiscal(TestCase):

    def setUp(self):
        usuario = Usuario(1, 'jose.silva', 'José da Silva')
        self.ape = Ape()
        self.ape.despesas = [Despesa(usuario, 20, datetime(2013, 10, 15)), 
                             Despesa(usuario, 30, datetime(2013, 10, 16)),
                             Despesa(usuario, 80, datetime(2013, 10, 17)),
                             Despesa(usuario, 50, datetime(2013, 12, 16))]

        self.mes_fiscal = MesFiscal(self.ape, 
                                    datetime(2013,10,10), 
                                    datetime(2013,11,10))
    
    def test_deve_conter_data_inicio(self):
        self.assertTrue(hasattr(self.mes_fiscal, "data_inicio"))

    def test_deve_conter_data_fim(self):
        self.assertTrue(hasattr(self.mes_fiscal, "data_fim"))

    def test_nao_deve_existir_sem_data_inicial_valida(self):
        with self.assertRaises(ValueError) as error:
            MesFiscal(self.ape, None, datetime(2013, 11, 10))

        self.assertEqual("data_inicio", str(error.exception))

    def test_nao_deve_existir_sem_data_fim_valida(self):
        with self.assertRaises(ValueError) as error:
            MesFiscal(self.ape, datetime(2013, 11, 10), None) 

        self.assertEqual("data_fim", str(error.exception))

    def test_deve_indicar_o_nome_do_mes(self):
        self.assertEqual('Outubro', self.mes_fiscal.nome_do_mes())

    def test_deve_listar_despesas_do_periodo(self):
        despesas = self.ape.despesas[:3]
        self.assertEqual(despesas, self.mes_fiscal.listar_despesas())

    def test_deve_calcular_total_das_despesas(self):
        despesas = self.mes_fiscal.listar_despesas()
        self.assertEqual(130, sum(d.valor for d in despesas))
