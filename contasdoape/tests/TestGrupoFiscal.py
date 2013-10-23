from contasdoape.models.DespesasRepository import DespesaRepository
from contasdoape.models.GrupoFiscal import GrupoFiscal
from contasdoape.models.Despesa import Despesa 
from unittest.mock import patch
from datetime import datetime
from unittest import TestCase

class TestGrupoFiscal(TestCase):
    def setUp(self):
        despesas = [ Despesa(10, 'A', datetime.now), 
                     Despesa(20, 'B', datetime.now),
                     Despesa(10, 'B', datetime.now) ]

        with patch.object(DespesaRepository, 'listar_despesas_do_periodo', return_value = despesas) as fake:
            self._grupo = GrupoFiscal(('2013-08-02', '2013-09-02'));
    
    def test_nao_deve_criar_sem_dicionario_de_autores(self):
        with self.assertRaises(ValueError) as error:
            GrupoFiscal(2)

        self.assertEqual('periodo', str(error.exception))

    def test_deve_indicar_o_devedor(self):
        self.assertEqual('A', self._grupo.obter_devedor())

    def test_deve_calcular_a_divida_de_um_autor(self):
        self.assertEqual(-10, self._grupo.calcular_divida('A'))

    def test_deve_retornar_os_autores(self):
        self.assertDictEqual({ 'A' : 10, 'B' : 30 }, self._grupo.obter_autores())
