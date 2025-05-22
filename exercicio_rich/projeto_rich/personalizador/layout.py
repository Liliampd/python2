from rich.layout import Layout

def criar_layout():
    layout = Layout(name="root")
    layout.split_column(
        Layout(name="cabecalho", size=3),
        Layout(name="corpo", ratio=1),
        Layout(name="rodape", size=3),
    )
    layout["corpo"].split_row(
        Layout(name="menu"),
        Layout(name="conteudo", ratio=2)
    )
    return layout
from rich.console import Console

console = Console()

def mostrar_layout_simples(texto, isArquivo):
    """
    Mostra um layout simples com o texto no corpo.
    Se isArquivo for True, lê o conteúdo de um arquivo.
    """
    if isArquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
        except FileNotFoundError:
            console.print("[bold red]Arquivo não encontrado.[/]")
            return

    layout = criar_layout()  # usa a função que você já fez
    layout["cabecalho"].update("[bold magenta]CABEÇALHO[/bold magenta]")
    layout["conteudo"].update(texto)
    layout["rodape"].update("[bold cyan]RODAPÉ[/bold cyan]")

    console.print(layout)
