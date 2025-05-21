from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

def criar_barra_progresso():
    return Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TextColumn("{task.completed}/{task.total}")
    )
