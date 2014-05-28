from contasdoape.models import Usuario
from unittest import TestCase


class TestDespesa(TestCase):

    def test_deve_conter_nome(self):
        usuario = Usuario(1, 'João')
        self.assertTrue(hasattr(usuario, 'nome'))

    def test_deve_conter_facebookid(self):
        usuario = Usuario(1, 'João')
        self.assertTrue(hasattr(usuario, 'facebook_id'))

    def test_nao_deve_existir_sem_nome(self):
        with self.assertRaises(ValueError) as error:
            Usuario(1, None)

        self.assertEqual('nome', str(error.exception))

    def test_nao_deve_existir_sem_facebookid(self):
        with self.assertRaises(ValueError) as error:
            Usuario(None, 'João')

        self.assertEqual('facebook_id', str(error.exception))
