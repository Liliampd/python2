# 🧭 Aventura no Labirinto

Um jogo de labirinto no terminal, feito com Python e a biblioteca `rich`, onde você controla um personagem até a saída do labirinto enfrentando obstáculos!

---

## 🎮 Como jogar

1. **Clone ou baixe o projeto no seu computador**
2. **Instale as dependências**:
```bash
pip install -r requirements.txt
-------------------------------------------------------------------------------------------------------------------

Rode o jogo com seus dados personalizados:
python main.py --name lili --color magenta --dificuldade facil

-------------------------------------------------------------------------------------------------------------------

Argumentos disponíveis

Argumento	Descrição	Exemplo
--name	Nome do jogador	--name lili
--color	Cor do painel e interface (rosa, cyan...)	--color rosa
--dificuldade	Nível do jogo: facil, medio ou dificil	--dificuldade medio

-------------------------------------------------------------------------------------------------------------------

Cores disponíveis
Você pode escolher uma das seguintes:

"vermelho": "red",
"verde": "green",
"azul": "blue",
"amarelo": "yellow",
"preto": "black",
"branco": "white",
"ciano": "cyan",
"magenta": "magenta",
"rosa": "magenta"



-------------------------------------------------------------------------------------------------------------------

🗺️ Sobre os níveis de dificuldade:

fácil: menos obstáculos e caminho direto;

médio: mais obstáculos e caminhos falsos;

difícil: labirinto desafiador com mais desvios.

-------------------------------------------------------------------------------------------------------------------
Estrutura do projeto

aventura_labirinto/
├── aventura_pkg/
│   ├── jogador.py
│   ├── labirinto.py
│   ├── painel.py
│   ├── utils.py
│   └── menu.py
├── labirinto/
│   ├── jogo.py
│   ├── mapa.py
│   └── teclado.py
├── main.py
├── requirements.txt
└── README.md

-------------------------------------------------------------------------------------------------------------------

Tecnologias utilizadas

Python 3.11
Biblioteca Rich

-------------------------------------------------------------------------------------------------------------------

🏁 Objetivo do jogo
Chegar até o ponto E (saída) movendo o personagem @ pelas direções:

W = cima

A = esquerda

S = baixo

D = direita

-------------------------------------------------------------------------------------------------------------------

🙌 Créditos
Desenvolvido por Liliam Santos como parte do desafio “Aventura no Labirinto” — com muito aprendizado e diversão! 🌟

-------------------------------------------------------------------------------------------------------------------
