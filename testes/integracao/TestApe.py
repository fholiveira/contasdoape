from unittest import TestCase
from mongoengine import connect
from contasdoape.models.Ape import Ape

class TestApe(TestCase):
    def setUp(self):
        self.conexao = connect('contasdoape-test')

    def test_criar_apartamento(self):
        Ape.objects.delete()

        Ape(nome = 'Novo Apto').save()

        ape = Ape.objects(nome = 'Novo Apto').first()
        self.assertIsNotNone(ape)
    
    def tearDown(self):
       self.conexao.drop_database('contasdoape-test')
