import argparse
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import criar_jogador, mover_jogador
from aventura_pkg.utils import imprime_instrucoes
from aventura_pkg.painel import exibir_painel_jogo

def main():
    parser = argparse.ArgumentParser(description="Jogo: Aventura no Labirinto!")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--color", default="cyan", help="Cor preferida do jogador")
    parser.add_argument("--dificuldade", default="facil", choices=["facil", "medio", "dificil"], help="Nível de dificuldade")
    parser.add_argument("--help", action="store_true", help="Exibe as instruções do jogo")

    args = parser.parse_args()

    console = Console()

    if args.help:
        imprime_instrucoes()
        return

    # Define quantidade de itens com base na dificuldade
    if args.dificuldade == "facil":
        qtd_itens = 3
    elif args.dificuldade == "medio":
        qtd_itens = 5
    else:
        qtd_itens = 8

    # Cria labirinto e jogador
    labirinto = criar_labirinto(qtd_itens=qtd_itens)
    jogador = criar_jogador()

    venceu = False
    while not venceu:
        console.clear()
        exibir_painel_jogo(jogador, args.name, args.color, args.dificuldade)
        imprimir_labirinto(labirinto)
        direcao = console.input("\nDigite a direção (W/A/S/D): ")
        venceu = mover_jogador(jogador, direcao, labirinto)

    console.print("\n🎉 Parabéns, você venceu o labirinto! 🎉", style="bold green")

if __name__ == "__main__":
    main()
