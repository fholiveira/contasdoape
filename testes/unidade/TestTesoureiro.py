from contasdoape.models.Tesoureiro import Tesoureiro
from contasdoape.models.Ape import Ape
from unittest import TestCase
from datetime import datetime


class TestDespesa(TestCase):

    def test_obter_mes_fiscal_deve_calcular_o_periodo_do_mes(self):
        ape = Ape(dia_do_acerto=1)
        mes = Tesoureiro(ape).obter_mes_fiscal(10, 2013)

        self.assertEquals(datetime(2013, 10, 1), mes.data_inicio)
        self.assertEquals(datetime(2013, 10, 31), mes.data_fim)

    def test_deve_listar_todos_os_meses_do_ano(self):
        meses = Tesoureiro(Ape()).listar_meses(2013)

        self.assertEquals(12, len(meses))
