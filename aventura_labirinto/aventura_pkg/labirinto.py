# aventura_pkg/labirinto.py

"""
Módulo labirinto
Contém funções para criação e impressão do labirinto.
"""

import random

def criar_labirinto(linhas=10, colunas=10, qtd_itens=5):
    """
    Cria um labirinto aleatório com obstáculos e itens.

    Args:
        linhas (int): número de linhas do labirinto
        colunas (int): número de colunas do labirinto
        qtd_itens (int): número de itens para o jogador coletar

    Returns:
        list: matriz representando o labirinto
    """
    # Criar o labirinto vazio (com espaço)
    labirinto = [[' ' for _ in range(colunas)] for _ in range(linhas)]

    # Colocar obstáculos (#)
    for _ in range(int(linhas * colunas * 0.2)):  # 20% de obstáculos
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        labirinto[i][j] = '#'

    # Colocar itens (*)
    for _ in range(qtd_itens):
        while True:
            i = random.randint(0, linhas - 1)
            j = random.randint(0, colunas - 1)
            if labirinto[i][j] == ' ':
                labirinto[i][j] = '*'
                break

    # Definir posição de entrada (E) e saída (S)
    labirinto[0][0] = 'E'
    labirinto[linhas-1][colunas-1] = 'S'

    return labirinto

def imprimir_labirinto(labirinto):
    """
    Imprime o labirinto na tela.

    Args:
        labirinto (list): matriz representando o labirinto
    """
    for linha in labirinto:
        print(' '.join(linha))
