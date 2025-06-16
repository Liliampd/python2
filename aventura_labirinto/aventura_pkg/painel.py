from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_painel_logo(nome, cor, dificuldade):
    texto = f"""
👋 Bem-vindo(a), {nome}!
🎨 Cor escolhida: {cor}
🎯 Nível de dificuldade: {dificuldade}

Prepare-se para encarar o desafio do labirinto!
    """
    console.print(Panel(texto, title="Aventura no Labirinto", subtitle="Boa sorte!", style=cor))
