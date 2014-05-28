from contasdoape.models import Convite, Usuario
from unittest import TestCase
from datetime import datetime


class TestConvite(TestCase):

    def test_nao_deve_existir_sem_destinatario(self):
        with self.assertRaises(ValueError) as error:
            Convite(Usuario(1, 'José'), None)

        self.assertEqual('destinatario', str(error.exception))

    def test_deve_datar_o_convite_ao_cria_lo(self):
        convite = Convite(Usuario(1, 'José'), '12342534')
        self.assertEquals(datetime.now().date(), convite.data.date())
