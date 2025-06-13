"""
Módulo painel.py
Exibe mensagens visuais usando a biblioteca rich.
"""

from rich.panel import Panel
from rich.console import Console
from rich.text import Text

console = Console()


def painel_boas_vindas(nome: str):
    """
    Exibe um painel de boas-vindas com o nome do jogador.
    """
    mensagem = Text(f"Bem-vindo(a), {nome}! Prepare-se para a Aventura no Labirinto!")
    painel = Panel(mensagem, title="🎮 Início do Jogo", subtitle="Use as teclas para se mover")
    console.print(painel)


def painel_vitoria(nome: str, pontos: int):
    """
    Exibe um painel de vitória com a pontuação final.
    """
    mensagem = Text(f"Parabéns, {nome}! Você venceu o labirinto! 🏆\nPontuação final: {pontos}")
    painel = Panel(mensagem, title="🎉 Vitória!", subtitle="Jogue novamente quando quiser")
    console.print(painel)


def painel_derrota(nome: str):
    """
    Exibe um painel de derrota.
    """
    mensagem = Text(f"Poxa, {nome}... você não conseguiu sair do labirinto 😢\nTente novamente!")
    painel = Panel(mensagem, title="💀 Fim de Jogo", subtitle="Boa sorte na próxima!")
    console.print(painel)
