from contasdoape.models.MesFiscal import MesFiscal
from contasdoape.models.Despesa import Despesa
from contasdoape.models.Usuario import Usuario
from contasdoape.models.Ape import Ape
from bson.objectid import ObjectId
from unittest.mock import patch
from unittest import TestCase
from datetime import datetime

class TestMesfiscal(TestCase):

    def setUp(self):
        self.ape = Ape()
        self.usuario = Usuario(1, 'José da Silva', id = ObjectId())
        self.usuario2 = Usuario(2, 'Pedro Pereira', id = ObjectId())
        self.ape.despesas = [Despesa(self.usuario, 20, datetime(2013, 10, 15), id = ObjectId()), 
                             Despesa(self.usuario, 30, datetime(2013, 10, 16), id = ObjectId()),
                             Despesa(self.usuario2, 80, datetime(2013, 10, 17), id = ObjectId()),
                             Despesa(self.usuario, 50, datetime(2013, 12, 16), id = ObjectId())]

        self.mes_fiscal = MesFiscal(self.ape, 
                                    datetime(2013,10,10), 
                                    datetime(2013,11,10))

        self.ape.save = lambda: None 
    
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
        self.assertEqual(130, self.mes_fiscal.calcular_saldo())

    def teste_deve_listar_despesas_de_um_autor(self):
        self.assertEquals(self.ape.despesas[2], self.mes_fiscal.obter_despesas(self.usuario2)[0])

    def teste_deve_listar_despesas_por_autor(self):
        por_autor = self.mes_fiscal.obter_despesas()
        autores = [a for a, d in por_autor.items()]
        self.assertCountEqual([self.usuario, self.usuario2], autores)

    def test_deve_disparar_exception_ao_tentar_remover_uma_despesa_que_nao_existe(self):
        with self.assertRaises(StopIteration):
            self.mes_fiscal.remover_despesa(self.usuario, 'salcifufu')

    def test_usuario_nao_deve_conseguir_excluir_despesa_de_outro_usuario(self):
        id = str(self.ape.despesas[0].id)
        with self.assertRaises(Exception):
            self.mes_fiscal.remover_despesa(self.usuario2, id)

    def test_deve_excluir_despesa(self):
        usuario = Usuario(1, 'Mário de Andrade', id = ObjectId())
        despesa = Despesa(usuario, 10, datetime.now(), id = ObjectId())
        
        self.ape.despesas.append(despesa)

        self.mes_fiscal.remover_despesa(usuario, str(despesa.id))

        self.assertNotIn(despesa, self.ape.despesas)
