from rich.layout import Layout

def criar_layout():
    layout = Layout(name="root")
    layout.split_column(
        Layout(name="cabecalho", size=3),
        Layout(name="corpo", ratio=1),
        Layout(name="rodape", size=3),
    )
    layout["corpo"].split_row(
        Layout(name="menu"),
        Layout(name="conteudo", ratio=2)
    )
    return layout
