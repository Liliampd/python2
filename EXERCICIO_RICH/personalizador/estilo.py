"""Módulo estilo - Funções que aplicam estilos ao texto com rich."""

from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
import os

console = Console()

def mostrar_em_markdown(texto: str, isArquivo: bool = False):
    """Exibe o conteúdo como se fosse um texto markdown."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto

    markdown = Markdown(conteudo)
    console.print(markdown)

def mostrar_com_estilo_personalizado(texto: str, isArquivo: bool = False):
    """Aplica estilos como cor, negrito e itálico no texto."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto

    estilo = Text(conteudo, style="bold italic magenta")
    console.print(estilo)
