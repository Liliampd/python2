"""
Módulo principal do jogo.
"""

from labirinto import mapa
from labirinto.utils import mostrar_labirinto
from rich import print

# Variável global para armazenar a posição atual do jogador
posicao_jogador = list(mapa.posicao_inicial)

def mover(direcao):
    """
    Move o jogador na direção escolhida.

    Args:
        direcao (str): 'w' (cima), 's' (baixo), 'a' (esquerda), 'd' (direita)
    """
    linha, coluna = posicao_jogador
    match direcao:
        case 'w':  # cima
            nova_posicao = (linha - 1, coluna)
        case 's':  # baixo
            nova_posicao = (linha + 1, coluna)
        case 'a':  # esquerda
            nova_posicao = (linha, coluna - 1)
        case 'd':  # direita
            nova_posicao = (linha, coluna + 1)
        case _:  # opção inválida
            print("[red]Movimento inválido![/red]")
            return

    # Verifica se a nova posição é válida
    if mapa.labirinto[nova_posicao[0]][nova_posicao[1]] != '#':
        posicao_jogador[0], posicao_jogador[1] = nova_posicao
    else:
        print("[yellow]Parede! Não é possível mover nessa direção.[/yellow]")

def verificar_saida():
    """
    Verifica se o jogador chegou na saída.
    """
    linha, coluna = posicao_jogador
    if mapa.labirinto[linha][coluna] == 'E':
        return True
    return False

def iniciar_jogo():
    """
    Inicia o jogo.
    """
    print("[bold blue]Bem-vindo à Aventura no Labirinto![/bold blue]")
    print("Controles: w (cima), s (baixo), a (esquerda), d (direita), q (sair)")

    while True:
        mostrar_labirinto(mapa.labirinto, tuple(posicao_jogador))
        
        direcao = input("Digite a direção (w/s/a/d) ou q para sair: ").lower()

        if direcao == 'q':
            print("[green]Você saiu do jogo. Até a próxima![/green]")
            break

        mover(direcao)

        if verificar_saida():
            print("[bold green]Parabéns! Você encontrou a saída![/bold green]")
            break
