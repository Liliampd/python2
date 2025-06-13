"""
Módulo labirinto
Contém funções para criação e impressão do labirinto.
"""

import random
from rich.console import Console
from rich.table import Table

console = Console()

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

    # Definir posição de entrada (S) e saída (E)
    labirinto[0][0] = 'S'  # Início
    labirinto[linhas-1][colunas-1] = 'E'  # Fim

    return labirinto

def imprimir_labirinto(labirinto, jogador_posicao=None):
    """
    Imprime o labirinto na tela com destaque para jogador, obstáculos e itens.

    Args:
        labirinto (list): matriz representando o labirinto
        jogador_posicao (tuple): posição (linha, coluna) do jogador (opcional)
    """
    tabela = Table(show_header=False, box=None, padding=(0, 1))

    for _ in range(len(labirinto[0])):
        tabela.add_column()

    for i, linha in enumerate(labirinto):
        nova_linha = []
        for j, celula in enumerate(linha):
            if jogador_posicao == (i, j):
                nova_linha.append("[bold green]@[/]")  # jogador
            elif celula == "#":
                nova_linha.append("[red]#[/]")
            elif celula == "*":
                nova_linha.append("[yellow]*[/]")
            elif celula == "S":
                nova_linha.append("[cyan]S[/]")
            elif celula == "E":
                nova_linha.append("[cyan]E[/]")
            else:
                nova_linha.append(" ")
        tabela.add_row(*nova_linha)

    console.print(tabela)
