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

from JogoDaVida import JogoDaVida, ValorEstruturalInvalido


class TestJogoDaVida(unittest.TestCase):
    def setUp(self):
        self.jdv = JogoDaVida(nlins=8, ncols=10, pop_baixa=2, pop_alta=3)

    def test_property_nlins(self):
        self.assertEqual(self.jdv.nlins, 8)

    def test_property_ncols(self):
        self.assertEqual(self.jdv.ncols, 10)

    def test_property_pop_baixa(self):
        self.assertEqual(self.jdv.pop_baixa, 2)

    def test_property_pop_alta(self):
        self.assertEqual(self.jdv.pop_alta, 3)

    def test_property_matriz(self):
        elementos_matriz = len(self.jdv.matriz_jogo)
        self.assertEqual(elementos_matriz, 80)

    def test_levanta_excecao_ncols_invalido(self):
        with self.assertRaises(ValorEstruturalInvalido) as vl:
            jogodavida = JogoDaVida(ncols=-1)

        errormsg = vl.exception.value
        self.assertEqual(errormsg, "Numero de colunas menor que zero!")

    def test_levanta_excecao_nlins_invalido(self):
        with self.assertRaises(ValorEstruturalInvalido) as vl:
            jogodavida = JogoDaVida(nlins=-1)

        errormsg = vl.exception.value
        self.assertEqual(errormsg, "Numero de linhas menor que zero!")

    def test_nlins_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.jdv.nlins = 7

    def test_ncols_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.jdv.ncols = 7

    def test_pop_alta_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.jdv.pop_alta = 7

    def test_pop_baixa_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.jdv.pop_baixa = 7

    def test_matriz_jogo_somente_leitura(self):
        with self.assertRaises(AttributeError):
            self.jdv.matriz_jogo = 7

    def test_conversao_par_coordenada_para_unidim(self):
        conv_zero = self.jdv._par_coord_para_unidim(0, 0)
        self.assertEqual(conv_zero, 0)
        conv_limit = self.jdv._par_coord_para_unidim(7, 9)
        self.assertEqual(conv_limit, 79)

    def test_conversao_unidim_par_coordenada(self):
        conv_zero = self.jdv._unidim_para_par_coord(0)
        self.assertEqual(conv_zero, (0, 0))
        conv_limit = self.jdv._unidim_para_par_coord(79)
        self.assertEqual(conv_limit, (7, 9))

    def test_levanta_excecao_modulo_invalido(self):
        with self.assertRaises(ValorEstruturalInvalido) as vl:
            self.jdv.preenche_celulas_modular(modulo=-1, espaco=3)

        errormsg = vl.exception.value
        self.assertEqual(
            errormsg,
            "Valor de Modulo invalido. Deve ser maior do que zero.")

    def test_levanta_excecao_espaco_invalido(self):
        with self.assertRaises(ValorEstruturalInvalido) as vl:
            self.jdv.preenche_celulas_modular(modulo=3, espaco=-1)

        errormsg = vl.exception.value
        self.assertEqual(
            errormsg,
            "Valor de Espaco invalido. Deve ser maior do que zero.")

    def test_pos_dentro_dos_limites(self):
        dentro_limites_um = self.jdv._dentro_dos_limites(0, 0)
        dentro_limites_dois = self.jdv._dentro_dos_limites(7, 9)

        self.assertTrue(dentro_limites_um)
        self.assertTrue(dentro_limites_dois)

        abaixo_limites_um = self.jdv._dentro_dos_limites(0, -1)
        abaixo_limites_dois = self.jdv._dentro_dos_limites(-1, 0)
        self.assertFalse(abaixo_limites_um)
        self.assertFalse(abaixo_limites_dois)

        acima_limites_um = self.jdv._dentro_dos_limites(7, 10)
        acima_limites_dois = self.jdv._dentro_dos_limites(8, 9)
        self.assertFalse(acima_limites_um)
        self.assertFalse(acima_limites_dois)

    def test_conta_vizinhos_vazio(self):
        vizinhos = self.jdv._conta_vizinhos(0)
        self.assertEqual(vizinhos, 0)

    def test_conta_vizinhos_preenchido(self):
        self.jdv.preenche_celulas_modular(modulo=3, espaco=5)
        vizinhos = self.jdv._conta_vizinhos(7)
        self.assertEqual(vizinhos, 4)


if __name__ == '__main__':
    unittest.main()
