from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_menu():
    while True:
        console.print(Panel("[bold cyan]=== MENU PRINCIPAL ===[/bold cyan]\n\n"
                            "1️⃣  Começar o jogo\n"
                            "2️⃣  Ver instruções\n"
                            "3️⃣  Sair\n", title="Menu"))

        opcao = input("Digite a opção desejada (1/2/3): ")

        if opcao == "1":
            return "jogar"
        elif opcao == "2":
            return "instrucoes"
        elif opcao == "3":
            return "sair"
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")
