from rich.panel import Panel
from rich.align import Align

def criar_painel(texto, titulo=""):
    return Panel(
        Align.center(texto, vertical="middle"),
        title=titulo,
        border_style="blue"
    )
