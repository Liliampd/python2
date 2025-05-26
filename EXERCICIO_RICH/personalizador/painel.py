"""Módulo painel - Funções que usam painéis do Rich para exibir texto formatado."""

from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def painel_simples(texto: str, isArquivo: bool = False):
    """Exibe o texto dentro de um painel simples."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto

    painel = Panel(conteudo, title="Painel Simples")
    console.print(painel)

def painel_com_estilo(texto: str, isArquivo: bool = False):
    """Exibe o texto dentro de um painel com borda dupla e cor."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto

    painel = Panel(conteudo, title="Painel Estilizado", border_style="bold magenta", title_align="left")
    console.print(painel)
