# _*_ coding: utf-8 _*_

# @brief    Arquivo principal do projeto
# @author   Gustavo Pereira
# @date     4/12/2015

from JogoDaVida import JogoDaVida

# Constante que determina quantos 'passos' do jogo serao executados
QUANTIDADE_DE_PASSOS = 10


def main():
    jdv = JogoDaVida()

    # Preenchimento das celulas pelo metodo modular: sao preenchidas
    # modulo celulas e entao sao deixadas espaco celulas em branco, repetindo o
    # padrao ate o fim do campo
    jdv.preenche_celulas_modular(modulo=3, espaco=5)

    # Impressao que mostra a matriz inicial do jogo
    jdv.mostra_matriz_jogo()

    for i in range(0, QUANTIDADE_DE_PASSOS):
        jdv.executa_passo_jogo()
        jdv.mostra_matriz_jogo()


if __name__ == '__main__':
    main()
