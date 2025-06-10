import argparse
from rich.console import Console
from aventura_pkg.jogador import Jogador
from aventura_pkg.labirinto import Labirinto
from aventura_pkg.utils import imprime_instrucoes
from aventura_pkg.menu import exibir_menu

console = Console()

def main():
    # Menu inicial
    acao = exibir_menu()

    if acao == "instrucoes":
        imprime_instrucoes()
        return
    elif acao == "sair":
        console.print("[bold magenta]Até a próxima! 👋[/bold magenta]")
        return

    # Argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Jogo de Aventura no Labirinto")

    parser.add_argument("--name", type=str, help="Nome do jogador")
    parser.add_argument("--color", type=str, help="Cor favorita do jogador")
    parser.add_argument("--dificuldade", type=str, choices=["facil", "medio", "dificil"], default="facil", help="Nível de dificuldade")

    args = parser.parse_args()

    nome = args.name if args.name else "Aventureiro(a)"
    cor = args.color if args.color else "azul"
    dificuldade = args.dificuldade

    console.print(f"[bold yellow]Jogador:[/bold yellow] {nome}, [bold yellow]Cor:[/bold yellow] {cor}, [bold yellow]Dificuldade:[/bold yellow] {dificuldade}")

    # Criar jogador e labirinto
    jogador = Jogador(nome, cor)
    labirinto = Labirinto(dificuldade)

    # Exibir labirinto inicial
    labirinto.exibir(jogador)

    # Loop de jogo (simples por enquanto)
    while True:
        comando = input("Digite um comando (W/A/S/D para mover ou Q para sair): ").lower()

        if comando == "q":
            console.print("[bold red]Saindo do jogo...[/bold red] 👋")
            break

        if comando in ["w", "a", "s", "d"]:
            jogador.mover(comando, labirinto)
            labirinto.exibir(jogador)
        else:
            console.print("[red]Comando inválido. Use W, A, S, D ou Q.[/red]")

if __name__ == "__main__":
    main()
