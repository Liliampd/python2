# jogador.py

from pynput import keyboard

# Variáveis globais para posição e pontuação
posicao_jogador = [0, 0]
pontuacao = 0
labirinto = []

def iniciar_jogador(lab):
    global posicao_jogador, pontuacao, labirinto
    labirinto = lab
    posicao_jogador = encontrar_entrada()
    pontuacao = 0
    print(f"\nJogador iniciado na posição {posicao_jogador} com pontuação {pontuacao}")

def encontrar_entrada():
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == 'E':
                return [i, j]
    return [0, 0]

def mover():
    def on_press(tecla):
        global posicao_jogador

        try:
            if tecla.char == 'w':
                mover_para(-1, 0)
            elif tecla.char == 's':
                mover_para(1, 0)
            elif tecla.char == 'a':
                mover_para(0, -1)
            elif tecla.char == 'd':
                mover_para(0, 1)
        except AttributeError:
            pass  # Ignora teclas especiais

    print("Use as teclas W A S D para mover. Pressione ESC para sair.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def mover_para(dx, dy):
    global posicao_jogador, pontuacao

    nova_pos = [posicao_jogador[0] + dx, posicao_jogador[1] + dy]

    # Verifica se está dentro do labirinto
    if (0 <= nova_pos[0] < len(labirinto)) and (0 <= nova_pos[1] < len(labirinto[0])):
        celula = labirinto[nova_pos[0]][nova_pos[1]]

        if celula != '#':  # Se não for parede
            posicao_jogador[:] = nova_pos
            if celula == '*':
                pontuar()
                labirinto[nova_pos[0]][nova_pos[1]] = ' '
            print(f"Movido para {posicao_jogador}. Pontuação: {pontuacao}")

            if celula == 'S':
                print("\nVocê venceu o jogo!")
                exit()

def pontuar():
    global pontuacao
    pontuacao += 10
    print(f"Item coletado! Nova pontuação: {pontuacao}")
