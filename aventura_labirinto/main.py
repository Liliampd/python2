# main.py

from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover

def main():
    print("=== Aventura no Labirinto ===\n")

    # Cria o labirinto
    lab = criar_labirinto()
    imprimir_labirinto(lab)

    # Inicia o jogador
    iniciar_jogador(lab)

    # Começa a movimentação
    mover(lab)


if __name__ == "__main__":
    main()
