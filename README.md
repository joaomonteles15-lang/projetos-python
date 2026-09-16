# projeto python
# 🎯 Jogo de Adivinhação

Jogo simples com interface gráfica feito em Python, usando a biblioteca `tkinter`.

## Como funciona

O programa sorteia um número aleatório entre **1 e 100**. O jogador digita um palpite e clica em "Chutar":

- Se o palpite for **maior** que o número secreto, o jogo avisa para tentar um número menor.
- Se for **menor**, avisa para tentar um número maior.
- Se **acertar**, mostra quantas tentativas foram usadas e desativa o botão de chutar.

Um botão **"Jogar de novo"** sorteia um novo número e reinicia o contador de tentativas.

## Tecnologias usadas

- Python 3
- `tkinter` (interface gráfica, já vem instalado com o Python)
- `random` (para sortear o número secreto)

## Como rodar

1. Tenha o Python 3 instalado.
2. Clone este repositório ou baixe o arquivo `jogo_adivinhacao_gui.py`.
3. No terminal, dentro da pasta do projeto, rode:

   ```bash
   python jogo_adivinhacao_gui.py
   ```

4. A janela do jogo vai abrir automaticamente.

## O que aprendi com esse projeto

- Criação de interfaces gráficas com `tkinter` (janelas, labels, botões, caixas de texto)
- Funções de callback (funções ligadas a eventos de clique)
- Uso de `global` para modificar variáveis fora do escopo da função
- Tratamento de erros com `try`/`except`
- Lógica de comparação e contagem de tentativas

## Próximos passos (ideias de melhoria)

- Adicionar um limite máximo de tentativas
- Mostrar histórico de palpites já tentados
- Permitir escolher o intervalo de números (ex: 1 a 1000)
