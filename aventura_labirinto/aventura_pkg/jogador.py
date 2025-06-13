"""
Módulo jogador
Responsável pelos movimentos e status do jogador no labirinto.
"""

def criar_jogador():
    """
    Cria o jogador na posição inicial do labirinto.

    Returns:
        dict: informações do jogador (posição, pontos, etc.)
    """
    return {
        "linha": 0,
        "coluna": 0,
        "pontos": 0,
        "itens_coletados": 0
    }

def mover_jogador(jogador, direcao, labirinto):
    """
    Move o jogador para uma nova posição, se possível.

    Args:
        jogador (dict): informações do jogador
        direcao (str): direção (W, A, S, D)
        labirinto (list): matriz do labirinto

    Returns:
        bool: True se o jogador venceu o jogo, False caso contrário
    """
    movimentos = {
        "W": (-1, 0),
        "A": (0, -1),
        "S": (1, 0),
        "D": (0, 1)
    }

    direcao = direcao.upper()
    if direcao not in movimentos:
        return False

    delta_linha, delta_coluna = movimentos[direcao]
    nova_linha = jogador["linha"] + delta_linha
    nova_coluna = jogador["coluna"] + delta_coluna

    # Verificar se está dentro dos limites do labirinto
    if 0 <= nova_linha < len(labirinto) and 0 <= nova_coluna < len(labirinto[0]):
        destino = labirinto[nova_linha][nova_coluna]

        if destino == "#":
            return False  # Bateu na parede

        if destino == "*":
            jogador["pontos"] += 10
            jogador["itens_coletados"] += 1

        # Atualizar posição
        jogador["linha"] = nova_linha
        jogador["coluna"] = nova_coluna

        # Verificar se chegou ao final
        if destino == "E":
            return True  # Vitória

    return False
