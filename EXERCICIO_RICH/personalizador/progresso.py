"""Módulo progresso - Funções que mostram barra de progresso com rich."""

from rich.console import Console
from rich.progress import track, Progress
import time
import os

console = Console()

def mostrar_com_progresso_lento(texto: str, isArquivo: bool = False):
    """Simula leitura lenta do texto com barra de progresso."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.readlines()
    else:
        conteudo = texto.split('\n')

    for linha in track(conteudo, description="Carregando..."):
        time.sleep(0.1)
        console.print(linha)

def mostrar_com_progresso_personalizado(texto: str, isArquivo: bool = False):
    """Mostra o texto com progresso personalizado (barra colorida)."""
    if isArquivo and os.path.exists(texto):
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.readlines()
    else:
        conteudo = texto.split('\n')

    with Progress() as progress:
        tarefa = progress.add_task("[cyan]Processando...", total=len(conteudo))
