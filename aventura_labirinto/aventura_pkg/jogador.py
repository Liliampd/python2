from pynput import keyboard

# Variáveis globais para a posição do jogador
jogador_pos = [0, 0]  # linha, coluna

# Pontuação
pontuacao = 0

# Itens do labirinto
itens = set()

def iniciar_jogador(labirinto, pos_inicial=(0, 0)):
    global jogador_pos, pontuacao, itens
    jogador_pos = list(pos_inicial)
    pontuacao = 0
    # Encontrar todos os '*' (itens) no labirinto
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == '*':
                itens.add((i, j))

def imprimir_labirinto(labirinto):
    for i, linha in enumerate(labirinto):
        linha_str = ''
        for j, celula in enumerate(linha):
            if [i, j] == jogador_pos:
                linha_str += 'P '  # P para indicar o jogador
            else:
                linha_str += celula + ' '
        print(linha_str)
    print(f'Pontuação: {pontuacao}')

def mover(labirinto):

    def on_press(tecla):
        global jogador_pos, pontuacao
        try:
            tecla_char = tecla.char.lower()
            nova_pos = jogador_pos.copy()

            if tecla_char == 'w':
                nova_pos[0] -= 1
            elif tecla_char == 's':
                nova_pos[0] += 1
            elif tecla_char == 'a':
                nova_pos[1] -= 1
            elif tecla_char == 'd':
                nova_pos[1] += 1
            elif tecla_char == 'q':
                # Sair do jogo
                print("Encerrando o jogo...")
                return False

            # Verificar se a nova posição é válida
            if 0 <= nova_pos[0] < len(labirinto) and 0 <= nova_pos[1] < len(labirinto[0]):
                if labirinto[nova_pos[0]][nova_pos[1]] != '#':
                    jogador_pos = nova_pos
                    pontuar()
                    # Limpar tela (no Windows funciona com 'cls')
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== Aventura no Labirinto ===")
                    imprimir_labirinto(labirinto)

                    # Verificar se chegou no final
                    if labirinto[jogador_pos[0]][jogador_pos[1]] == 'S':
                        print("\nParabéns, você chegou no final! 🎉")
                        return False

        except AttributeError:
            pass  # Ignorar outras teclas (ex: SHIFT, CTRL, etc)

    # Escutador de teclado
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def pontuar():
    global pontuacao
    pos_tuple = tuple(jogador_pos)
    if pos_tuple in itens:
        pontuacao += 10
        itens.remove(pos_tuple)
        print("Item coletado! +10 pontos")
