# _*_ coding: utf-8 _*_

# @brief    Classe que representa uma celula do jogo da vida
# @author   Gustavo Pereira
# @date     4/12/2015


class CelulaJogoDaVida:
    def __init__(self, viva=False, simbolo_viva='[X]', simbolo_morta='[ ]'):
        # Indica se celula esta viva
        self._viva = viva
        # Simbolos para impressao; Caso desejado, podem ser mudados da escolha
        # padrao
        self._simbolo_viva = simbolo_viva
        self._simbolo_morta = simbolo_morta

    # Colocando os atributos protegidos como somente-leitura.
    @property
    def viva(self):
        return self._viva

    @viva.setter
    def viva(self, v):
        raise AttributeError

    @property
    def simbolo_viva(self):
        return self._simbolo_viva

    @simbolo_viva.setter
    def simbolo_viva(self, v):
        raise AttributeError

    @property
    def simbolo_morta(self):
        return self._simbolo_morta

    @simbolo_morta.setter
    def simbolo_morta(self, v):
        raise AttributeError

    # @brief    Retorna o caracter que representa uma celula viva ou morta
    #           para a impressao
    def mostra_caracter_estado(self):
        if self._viva:
            return self._simbolo_viva
        return self._simbolo_morta

    # @brief    Sinaliza se a celula esta viva ou morta
    def esta_viva(self):
        return self._viva

    # @brief    Troca o estado de viva da celula: mata se vive e nasce se
    #           morta
    def muda_estado(self):
        self._viva = not self._viva

    # Os proximos dois metodos nao sao utilizados nesta implementacao,
    # mas considero importante disponibiliza-los

    # @brief    Faz com que a presente celula se torne viva.
    def nasce(self):
        self._viva = True

    # @brief    Faz com que a presente celula se torne morta.
    def morre(self):
        self._viva = False
