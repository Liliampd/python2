from time import sleep
from rich.progress import Progress

def barra_progresso(total=100, tempo=0.05):
    """
    Exibe uma barra de progresso animada até atingir o total.
    Por padrão, vai até 100, com 0.05 segundos entre os passos.
    """
    with Progress() as progress:
        tarefa = progress.add_task("[cyan]Carregando...", total=total)

        while not progress.finished:
            progress.update(tarefa, advance=1)
            sleep(tempo)
