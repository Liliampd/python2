# main.py
import argparse
from labirinto import jogo

def main():
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")
    parser.add_argument('--start', action='store_true', help='Inicia o jogo')

    args = parser.parse_args()

    if args.start:
        jogo.iniciar_jogo()
    else:
        print("Use --start para iniciar o jogo.")

if __name__ == "__main__":
    main()
