"""main.py — Interface de linha de comando para o pacote personalizador."""

import argparse
from personalizador import layout, painel, progresso, estilo

# Dicionário para mapear módulos e funções
modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

funcoes_disponiveis = {
    "layout": ["mostrar_titulo", "mostrar_regua"],
    "painel": ["mostrar_painel_simples", "mostrar_painel_com_borda"],
    "progresso": ["barra_simples", "barra_com_tarefa"],
    "estilo": ["mostrar_em_markdown", "mostrar_com_estilo_personalizado"]
}

# Argumentos do argparse
parser = argparse.ArgumentParser(description="Personalizador de texto com Rich")

parser.add_argument("texto", help="Texto ou caminho para um arquivo")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o texto é um caminho de arquivo")
parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys(), help="Escolha um dos módulos: layout, painel, progresso, estilo")
parser.add_argument("-f", "--funcao", required=True, help="Escolha a função do módulo. Veja as opções com -m")

args = parser.parse_args()

# Verifica se módulo e função são válidos
modulo = modulos.get(args.modulo)

if args.funcao not in funcoes_disponiveis[args.modulo]:
    print(f"Função inválida para o módulo '{args.modulo}'. Opções disponíveis: {funcoes_disponiveis[args.modulo]}")
else:
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)
