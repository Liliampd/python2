"""Módulo layout - Funções que usam recursos de layout da biblioteca Rich."""

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
import os

console = Console()

def exibir_colunas(texto: str, isArquivo: bool = False):
    ...

def exibir_paineis_lado_a_lado(texto: str, isArquivo: bool = False):
    ...

def mostrar_titulo(texto: str, isArquivo: bool = False):
    """Mostra o texto como título usando estilo de layout com Rich."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto

    console.rule(conteudo)
