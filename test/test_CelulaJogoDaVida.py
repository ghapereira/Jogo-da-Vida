# _*_ coding: utf-8 _*_
import unittest
import os
import sys

# Adiciona diretorio pai ao path, permitindo importar
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(os.getcwd(), os.path.expanduser(__file__))))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT))
sys.path.insert(1, PROJECT_ROOT)

from CelulaJogoDaVida import CelulaJogoDaVida


class TestCelulaJogoDaVida(unittest.TestCase):
    def setUp(self):
        self.celula = CelulaJogoDaVida(viva=False,
                                       simbolo_viva='[X]',
                                       simbolo_morta='[ ]')

    def test_init_viva(self):
        self.assertFalse(self.celula.viva)

    def test_init_simbolo_viva(self):
        self.assertEqual(self.celula.simbolo_viva, '[X]')

    def test_init_simbolo_morta(self):
        self.assertEqual(self.celula.simbolo_morta, '[ ]')

    def test_viva_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.celula.viva = False

    def test_simbolo_viva_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.celula.simbolo_viva = '[$]'

    def test_simbolo_morta_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.celula.simbolo_morta = '[#]'

    def test_muda_estado(self):
        self.celula.muda_estado()
        self.assertTrue(self.celula.viva)
        self.celula.muda_estado()
        self.assertFalse(self.celula.viva)

    def test_nasce(self):
        self.celula.nasce()
        self.assertTrue(self.celula.viva)

    def test_morre(self):
        self.celula.morre()
        self.assertFalse(self.celula.viva)


if __name__ == '__main__':
    unittest.main()
