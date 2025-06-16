from rich.console import Console
from rich.markdown import Markdown

def imprimir_instrucoes():
    console = Console()
    try:
        with open("instrucoes.txt", "r", encoding="utf-8") as f:
            texto = f.read()
            md = Markdown(texto)
            console.print(md)
    except FileNotFoundError:
        console.print("[red]Arquivo de instruções não encontrado.[/red]")
