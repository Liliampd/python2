"""
Módulo que contém o mapa do labirinto.
"""

# O labirinto é uma matriz de caracteres
# '#' = parede
# ' ' = caminho livre
# 'E' = saída (Exit)

labirinto = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', '#', '#', 'E', '#']
]

# Posição inicial do jogador (linha, coluna)
posicao_inicial = (1, 1)
