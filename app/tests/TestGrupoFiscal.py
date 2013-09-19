from models.GrupoFiscal import GrupoFiscal
from unittest import TestCase
from unittest.mock import patch

class TestGrupoFiscal(TestCase):
    def setUp(self):
        autores = { 'A' : 10, 'B' : 20 }
        with patch.object(GrupoFiscal, '_carregar_autores', return_value = autores) as fake:
            self._grupo = GrupoFiscal(('2013-08-02', '2013-09-02'));
    
    def test_nao_deve_criar_sem_dicionario_de_autores(self):
        with self.assertRaises(ValueError) as error:
            GrupoFiscal(2)

        self.assertEqual('periodo', str(error.exception))

    def test_deve_indicar_o_devedor(self):
        self.assertEqual('A', self._grupo.obter_devedor())

    def test_deve_calcular_a_divida_de_um_autor(self):
        self.assertEqual(-5, self._grupo.calcular_divida('A'))

    def test_deve_retornar_os_autores(self):
        self.assertDictEqual({ 'A' : 10, 'B' : 20 }, self._grupo.obter_autores())
