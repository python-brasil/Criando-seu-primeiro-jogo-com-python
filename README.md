# Criando seu primeiro jogo com python
O código acima é um jogo simples de Snake feito em Python utilizando a biblioteca Pygame. Aqui está um resumo das principais partes do código:

Inicialização do Pygame:
- O Pygame é inicializado com pygame.init().

Definição da Janela:
- Uma janela de tamanho 400x400 pixels é criada com o título "Jogo Snake Python Brasil".

Cores:
- Três cores são definidas: branco, preto e duas tonalidades de azul (para a cobra) e amarelo (para a comida).

Tamanho do Bloco e Velocidade:
- O tamanho do bloco da cobra é definido como 20 pixels e a velocidade do jogo é definida como 10.

Relógio para Controle de FPS:
- Um relógio é criado para controlar o FPS (frames por segundo) do jogo.

Função para Desenhar a Cobra:
- A função draw_snaake(snake) desenha a cobra na tela.

Função Principal do Jogo (game()):
- A cobra é representada como uma lista de segmentos, onde cada segmento é uma lista contendo as coordenadas x e y do segmento.
- A direção da cobra é controlada pelas teclas de seta.
- A comida é representada como um retângulo amarelo que aparece em uma posição aleatória na tela.

O jogo entra em um loop infinito onde:
- Verifica eventos do teclado e atualiza a direção da cobra.
- Move a cobra adicionando um novo segmento na frente e removendo o último segmento.
- Verifica se a cabeça da cobra colide com a comida e, se sim, gera uma nova posição aleatória para a comida.
- Desenha a comida, a cobra e atualiza a tela.
- Controla a velocidade do jogo com o relógio.
- O jogo continua rodando até que o jogador feche a janela.
  
Este é um jogo de Snake simples, onde o objetivo é controlar a cobra para comer a comida sem colidir com as bordas da janela ou com o próprio corpo.

## Rodando projeto

Clone o projeto

```bash
  git clone https://github.com/python-brasil/Criando-seu-primeiro-jogo-com-python.git
```
Recomandamos criar uma venv antes de instalar as dependências
```bash
  python -m venv venv
```
em Linux
```bash
  python3 -m venv venv
```
Instale as dependências

```bash
  pip install -r requirements.txt
```

em Linux

```bash
  pip3 install -r requirements.txt
```

## Screenshot

![Criando seu primeiro jogo com Python](https://github.com/python-brasil/Criando-seu-primeiro-jogo-com-python/assets/126124866/ea04dcac-c4ef-4ccd-aa04-3c8a1d546552)

## Infos de commits

- :package: novas funcionalidades
- :up: atualizações
- :ant: correções de bug
- :checkered_flag: release


## Nos acompanhe nas redes

- Instagram - [@python_brasil](https://www.instagram.com/python_brasil/)
- LinkedIn - [Comunidade Python Brasil](https://www.linkedin.com/company/comunidade-python-brasil)
- GitHub - [python-brasil](https://github.com/python-brasil)
- YouTube - [@Python_Brasil](https://www.youtube.com/@Python_Brasil)
- Pinterest - [Python Brasil](https://br.pinterest.com/pythonbrasil/)
- TikTok - [@python_brasil](https://www.tiktok.com/@python_brasil)

