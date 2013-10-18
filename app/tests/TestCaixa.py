from unittest import TestCase
from models.Despesa import Despesa
from models.Caixa import Caixa
from datetime import datetime
from unittest.mock import patch

class TestCaixa(TestCase):
    def test_nao_deve_aceitar_valores_nao_numericos(self):
        caixa = Caixa()
        with self.assertRaises(ValueError) as error:
            caixa.lancar_despesa(autor = 'Fernando', data = '2013-06-25', valor = 'aaa')

        self.assertEqual("valor", str(error.exception))
    
    def test_nao_deve_aceitar_data_fora_do_padrao_americano(self):
        caixa = Caixa()
        with self.assertRaises(ValueError) as error:
            caixa.lancar_despesa(autor = 'Fernando', data = '29-12-2015', valor = '13,5')

        self.assertEqual("data", str(error.exception))

    def test_deve_salvar_despesa(self):
        caixa = Caixa()

        with patch.object(Despesa, 'save') as mock_method:
            caixa.lancar_despesa('Fernando', '1992-05-10', '13')

        mock_method.assert_called() 
