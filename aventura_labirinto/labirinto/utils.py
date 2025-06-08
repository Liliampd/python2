"""
Módulo com funções auxiliares.
"""

def mostrar_labirinto(labirinto, posicao):
    """
    Função recursiva para mostrar o labirinto.
    
    Args:
        labirinto (list): matriz do labirinto
        posicao (tuple): posição atual do jogador (linha, coluna)
    """
    linha_atual = 0

    def mostrar_linha(labirinto, linha_atual):
        # Caso base: se já mostrou todas as linhas, para
        if linha_atual >= len(labirinto):
            return
        
        # Monta uma linha do labirinto com o jogador (P) na posição atual
        linha = ""
        for coluna, item in enumerate(labirinto[linha_atual]):
            if (linha_atual, coluna) == posicao:
                linha += "P "  # P = Player
            else:
                linha += item + " "
        
        print(linha)
        
        # Chamada recursiva para mostrar a próxima linha
        mostrar_linha(labirinto, linha_atual + 1)

    # Inicia a recursão
    mostrar_linha(labirinto, linha_atual)
