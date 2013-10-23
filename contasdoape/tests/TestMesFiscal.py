from contasdoape.models.DespesasRepository import DespesaRepository
from contasdoape.models.MesFiscal import MesFiscal
from contasdoape.models.Despesa import Despesa 
from unittest.mock import patch
from unittest import TestCase
from datetime import datetime

class TestMesfiscal(TestCase):

    def setUp(self):
        despesas = [ Despesa(10, 'A', datetime.now), 
                     Despesa(20, 'B', datetime.now),
                     Despesa(10, 'B', datetime.now) ]

        with patch.object(DespesaRepository, 'listar_despesas_do_periodo', return_value = despesas) as fake:
            self.mes_fiscal = MesFiscal(datetime(2013,10,10), datetime(2013,11,10))
    
    def test_deve_conter_data_inicio(self):
        self.assertTrue(hasattr(self.mes_fiscal, "data_inicio"))

    def test_deve_conter_data_fim(self):
        self.assertTrue(hasattr(self.mes_fiscal, "data_fim"))

    def test_nao_deve_existir_sem_data_inicial_valida(self):
        with self.assertRaises(ValueError) as error:
            MesFiscal("Data inicial", datetime(2013, 11, 10))

        self.assertEqual("data_inicio", str(error.exception))

    def test_nao_deve_existir_sem_data_fim_valida(self):
        with self.assertRaises(ValueError) as error:
            MesFiscal(datetime(2013, 11, 10), "sasasdasf f")

        self.assertEqual("data_fim", str(error.exception))

    def test_deve_indicar_o_nome_do_mes(self):
        self.assertEqual('Outubro', self.mes_fiscal.nome_do_mes())

    def test_deve_listar_despesas_do_periodo(self):
        despesas = [ Despesa(10, 'A', datetime.now), 
                     Despesa(20, 'B', datetime.now),
                     Despesa(10, 'B', datetime.now) ]

        with patch.object(DespesaRepository, 'listar_despesas_do_periodo', return_value = despesas) as fake:
            mes_fiscal = MesFiscal(datetime(2013,10,10), datetime(2013,11,10))
            mes_fiscal.listar_despesas()

        fake.assert_called_with(datetime(2013, 10, 10), datetime(2013, 11, 10))

    def test_deve_calcular_total_das_despesas(self):
        despesas = [ Despesa(10, 'A', datetime.now), 
                     Despesa(20, 'B', datetime.now),
                     Despesa(10, 'B', datetime.now) ]
        
        with patch.object(DespesaRepository, 'listar_despesas_do_periodo', return_value = despesas) as fake:
            saldo = self.mes_fiscal.calcular_saldo()
        
        self.assertEqual(40, saldo)

    def test_sumario(self):
        esperado = { 'nome' : 'Outubro',
                     'total' : '40.00',
                     'devedor' : 'A',
                     'valor_divida' : '-10.00',
                     'A' : '10.00',
                     'B' : '30.00' }

        despesas = [ Despesa(10, 'A', datetime.now), 
                     Despesa(20, 'B', datetime.now),
                     Despesa(10, 'B', datetime.now) ]
        
        with patch.object(DespesaRepository, 'listar_despesas_do_periodo', return_value = despesas) as fake:
            recebido = self.mes_fiscal.obter_sumario()
        
        self.assertEqual(esperado, recebido)
