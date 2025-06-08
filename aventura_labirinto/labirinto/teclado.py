"""
Módulo para demonstração do uso da biblioteca pynput (escutando o teclado).
"""

from pynput import keyboard
from rich import print

def on_press(key):
    """
    Função chamada quando uma tecla é pressionada.
    """
    try:
        print(f"[cyan]Você pressionou a tecla: {key.char}[/cyan]")
    except AttributeError:
        print(f"[magenta]Tecla especial pressionada: {key}[/magenta]")

def escutar_teclado():
    """
    Inicia o listener do teclado.
    """
    print("[bold blue]Pressione teclas (ESC para sair do listener)[/bold blue]")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
