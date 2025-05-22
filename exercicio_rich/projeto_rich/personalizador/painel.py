from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def criar_painel(texto, titulo=""):
    return Panel(
        Align.center(texto, vertical="middle"),
        title=titulo,
        border_style="blue"
    )

def painel_simples(texto, isArquivo):
    """
    Mostra o texto dentro de um painel azul.
    Se isArquivo for True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
        except FileNotFoundError:
            console.print("[bold red]Arquivo não encontrado.[/]")
            return

    panel = criar_painel(texto, titulo="Painel Simples")
    console.print(panel)

def painel_com_borda(texto, isArquivo):
    """
    Mostra o texto dentro de um painel com borda amarela.
    Se isArquivo for True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
        except FileNotFoundError:
            console.print("[bold red]Arquivo não encontrado.[/]")
            return

    panel = Panel(
        Align.center(texto, vertical="middle"),
        title="⚠️ Painel com Borda",
        border_style="yellow"
    )
    console.print(panel)
