from contasdoape.models import Despesa, Usuario, Relatorio, Divida
from bson.objectid import ObjectId
from unittest import TestCase
from datetime import datetime


class Testrelatorio(TestCase):

    def setUp(self):
        self.usuario1 = Usuario(1, 'Walter Kovacs', id=ObjectId())
        self.usuario2 = Usuario(2, 'Dan Dreiberg', id=ObjectId())
        self.gastos = {self.usuario1: [Despesa(self.usuario1,
                                               30,
                                               datetime(2013, 10, 15),
                                               id=ObjectId()),
                                       Despesa(self.usuario2,
                                               40,
                                               datetime(2013, 10, 16),
                                               id=ObjectId())],
                       self.usuario2: [Despesa(self.usuario1,
                                               530,
                                               datetime(2013, 10, 17),
                                               id=ObjectId()),
                                       Despesa(self.usuario2,
                                               60,
                                               datetime(2013, 10, 18),
                                               id=ObjectId())]}

    def test_deve_calcular_valor_total(self):
        relatorio = Relatorio(self.gastos, self.usuario1)
        self.assertEquals(180, relatorio.valor_total())

    def test_deve_calcular_valor_medio(self):
        relatorio = Relatorio(self.gastos, self.usuario1)
        self.assertEquals(90, relatorio.valor_medio())

    def test_deve_calcular_valor_gasto_pelo_usuario(self):
        relatorio = Relatorio(self.gastos, self.usuario1)
        self.assertEquals(70, relatorio.valor_gasto_pelo_usuario())

    def test_deve_calcular_valor_total(self):
        relatorio = Relatorio(self.gastos, self.usuario1)
        self.assertEquals(180, relatorio.valor_total())

    def test_deve_dizer_que_um_usuario_devedor_tem_relatorio(self):
        relatorio = Relatorio(self.gastos, self.usuario1)
        self.assertTrue(relatorio.usuario_esta_devendo())

    def test_deve_dizer_que_um_usuario_nao_devedor_nao_tem_relatorio(self):
        relatorio = Relatorio(self.gastos, self.usuario2)
        self.assertFalse(relatorio.usuario_esta_devendo())

    def test_deve_cacular_a_relatorio_do_usuario_devedor(self):
        relatorio = Relatorio(self.gastos, self.usuario1)
        self.assertEquals({self.usuario2: Divida(total_gasto=110, saldo=20)},
                          relatorio.divida_relativa())

    def test_deve_cacular_os_usuarios_que_devem_a_um_usuario_credor(self):
        relatorio = Relatorio(self.gastos, self.usuario2)
        self.assertEquals({self.usuario1: Divida(total_gasto=70, saldo=20)},
                          relatorio.divida_relativa())
