from contasdoape.models import MesFiscal, Despesa, Usuario, Ape
from bson.objectid import ObjectId
from mongoengine import connect
from unittest import TestCase
from datetime import datetime


class TestMesFiscal(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conexao = connect('contasdoape-test')

    def _criar_ape(self):
        usuario = Usuario('1', 'Edward Blake')
        usuario2 = Usuario('2', 'Walter Kovacs')
        usuario.save()
        usuario2.save()

        despesas = [Despesa(usuario, 20, datetime(2013, 10, 15), id=ObjectId()),
                    Despesa(usuario, 30, datetime(2013, 10, 16), id=ObjectId()),
                    Despesa(usuario2, 80, datetime(2013, 10, 17), id=ObjectId()),
                    Despesa(usuario, 50, datetime(2013, 12, 16), id=ObjectId())]

        ape = Ape()
        ape.membros.append(usuario)
        ape.membros.append(usuario2)
        ape.despesas = despesas
        ape.save()

        return ape

    def setUp(self):
        Usuario.objects().delete()
        Ape.objects.delete()

        self.ape = self._criar_ape()
        self.mes_fiscal = MesFiscal(self.ape,
                                    datetime(2013, 10, 10),
                                    datetime(2013, 11, 10))

    def test_deve_excluir_despesa(self):
        despesa = self.ape.despesas[0]
        self.mes_fiscal.remover_despesa(self.ape.membros[0], str(despesa.id))

        self.assertNotIn(despesa, Ape.objects().first().despesas)

    @classmethod
    def tearDownClass(cls):
        cls.conexao.drop_database('contasdoape-test')
