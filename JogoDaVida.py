# _*_ coding: utf-8 _*_

# @brief    Classe que representa o jogo da vida em si
# @author   Gustavo Pereira
# @date     4/12/2015

from CelulaJogoDaVida import CelulaJogoDaVida

# Tamanho do campo de jogo, que e representado por uma matriz NLINS x NCOLS
NLINS = 8
NCOLS = 10

# Constantes do jogo, que determinam valores para nascimento e morte de celulas
BAIXA_POP = 2
ALTA_POP = 3


class ValorEstruturalInvalido(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class JogoDaVida:
    def __init__(self, nlins=NLINS, ncols=NCOLS, pop_baixa=BAIXA_POP,
                 pop_alta=ALTA_POP):
        if nlins < 0:
            raise ValorEstruturalInvalido("Numero de linhas menor que zero!")
        if ncols < 0:
            raise ValorEstruturalInvalido("Numero de colunas menor que zero!")

        self._nlins = nlins
        self._ncols = ncols

        # A representacao interna da matriz de jogo e um vetor unidimensional.
        # O metodo par_coord_para_unidim e responsavel pela conversao de
        # coordenadas bidimensionais para unidimensionais
        self._matriz_jogo = []

        self._tamanho_total = nlins * ncols

        # Pelas regras do jogo, qualquer celula viva com menos do que
        # pop_baixa vizinhos morre por solidao, e com mais do que
        # pop_alta vizinhos morre por superpopulacao. Celulas vivas
        # so permanecem vivas com um pop_baixa <= n <= pop_alta, n
        # sendo o numero de vizinhos. Celulas mortas se tornam vivas
        # com pop_alta vizinhos.
        self._pop_baixa = pop_baixa
        self._pop_alta = pop_alta

        # Preenche o jogo inicial com celulas vazias
        for i in range(0, self._tamanho_total):
            self._matriz_jogo.append(CelulaJogoDaVida())

    # Atributos transformados em propriedades para manter somente-leitura
    @property
    def nlins(self):
        return self._nlins

    @nlins.setter
    def nlins(self, v):
        raise AttributeError

    @property
    def ncols(self):
        return self._ncols

    @ncols.setter
    def ncols(self, v):
        raise AttributeError

    @property
    def matriz_jogo(self):
        return self._matriz_jogo

    @matriz_jogo.setter
    def matriz_jogo(self, v):
        raise AttributeError

    @property
    def pop_baixa(self):
        return self._pop_baixa

    @pop_baixa.setter
    def pop_baixa(self, v):
        raise AttributeError

    @property
    def pop_alta(self):
        return self._pop_alta

    @pop_alta.setter
    def pop_alta(self, v):
        raise AttributeError

    # @brief    Converte um par de coordenadas cartesianas para um indice do
    #           espaco unidimensional
    def _par_coord_para_unidim(self, i, j):
        return i * self._ncols + j

    # @brief    Converte uma coordenada unidimensional para um par de
    #           coordenadas cartesianas
    def _unidim_para_par_coord(self, coord):
        j = coord % self._ncols
        # floor div
        i = (coord - j) // self._ncols

        return i, j

    # @brief    Funcao basica de exibicao de resultados
    def mostra_matriz_jogo(self):
        for i in range(0, self._nlins):
            linha_impressao = ''
            for j in range(0, self._ncols):
                coord = self._par_coord_para_unidim(i, j)
                linha_impressao += \
                    self._matriz_jogo[coord].mostra_caracter_estado()
            # Apos preparar a linha, imprime
            print(linha_impressao)

        print('\n')

    # @brief    Este metodo preenche as celulas com entes vivos da seguinte
    #           maneira:
    #           Em sequencia se colocam modulo celulas vivas. Apos isto,
    #           espaco celulas sao deixadas vazias. Novamente, modulo celulas
    #           sao colocadas e assim sucessivamente ate o fim da matriz de
    #           jogo
    def preenche_celulas_modular(self, modulo, espaco):
        mod_msg = "Valor de Modulo invalido. Deve ser maior do que zero."
        esp_msg = "Valor de Espaco invalido. Deve ser maior do que zero."

        if modulo < 0:
            raise ValorEstruturalInvalido(mod_msg)
        if espaco < 0:
            raise ValorEstruturalInvalido(esp_msg)

        m = modulo
        e = espaco

        for i in range(0, self._nlins):
            for j in range(0, self._ncols):
                coord = self._par_coord_para_unidim(i, j)
                # Preenche as celulas como vivas
                if m > 0:
                    self._matriz_jogo[coord].nasce()
                    m -= 1
                # Realiza o salto. Considero que este metodo so sera chamado
                # numa matriz vazia.
                else:
                    e -= 1
                    if e == 0:
                        m = modulo
                        e = espaco

    # @brief    Verifica se coordenada esta dentro dos limites da matriz
    def _dentro_dos_limites(self, i, j):
        if i < 0 or j < 0:
            return False
        if i >= self._nlins or j >= self._ncols:
            return False

        return True

    # @brief    Obtem o numero de vizinhos
    def _conta_vizinhos(self, posicao):
        x, y = self._unidim_para_par_coord(posicao)

        vizinhos = 0

        # Procura os vizinhos atraves do expediente de encontrar
        # celulas imediatamente proximas a direita e a esquerda, acima e
        # abaixo
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Evitando a propria celula
                if not (i == 0 and j == 0):
                    novo_x = x + i
                    novo_y = y + j
                    if self._dentro_dos_limites(novo_x, novo_y):
                        pos_vizinho = \
                            self._par_coord_para_unidim(novo_x, novo_y)
                        if self._matriz_jogo[pos_vizinho].esta_viva():
                            vizinhos += 1

        return vizinhos

    # @brief    Metodo principal de execucao, aplica as regras a um estado
    #           da matriz
    def executa_passo_jogo(self):
        lista_mudanca_estado = []

        # Verifica quais celulas devem mudar o estado (nascer/morrer),
        # agendando a mudanca para um loop posterior
        for i in range(0, self._tamanho_total):
            vizinhos = self._conta_vizinhos(i)

            # Celulas vivas so permanecem vivas com um
            # pop_baixa <= n <= pop_alta, n sendo o numero de vizinhos.
            if self._matriz_jogo[i].esta_viva():
                if (vizinhos < self._pop_baixa) or (vizinhos > self._pop_alta):
                    lista_mudanca_estado.append(i)
            #  Celulas mortas se tornam vivas com exatamente pop_alta vizinhos.
            else:
                if vizinhos == self._pop_alta:
                    lista_mudanca_estado.append(i)

        # Aplica mudancas determinadas no estagio anterior
        for i in lista_mudanca_estado:
            self._matriz_jogo[i].muda_estado()
