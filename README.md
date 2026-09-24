# Troco Ambicioso (Simulador com Algoritmo Guloso)

Um minigame de terminal desenvolvido em Python onde o jogador atua como caixa de uma loja. O objetivo é entregar o troco correto para o cliente utilizando a **menor quantidade de moedas possível** antes que o tempo acabe. 

O projeto utiliza o **Algoritmo Guloso (Greedy Algorithm)** para calcular matematicamente o gabarito do troco perfeito a cada rodada.

## Estudantes

|Matrícula|Aluno|
|---|---|
|251023282|Josef Wojtyla Barros de Souza|
|251020226|Eduardo de Sousa Brito|

## Pré-requisitos

Para rodar este jogo, você precisará ter o **Python 3.x** instalado na sua máquina.

## Como Rodar o Jogo

O jogo utiliza a biblioteca `curses` para desenhar a interface no terminal. O processo de execução varia um pouco dependendo do seu Sistema Operacional:

> Linux (Ubuntu, Debian, etc) e macOS
No Linux e no macOS, a biblioteca `curses` já vem embutida por padrão na instalação do Python.
Abra o seu terminal, navegue até a pasta do projeto e rode:

```bash
python main.py
```

> **Windows:** não traz a biblioteca `curses` nativamente. Por isso, antes de rodar o jogo pela primeira vez, precisa instalar um pacote auxiliar usando o `pip`:
1. Abra o terminal e cole este comando:
```bash
pip install windows-curses
```
2. Agora é só rodar o jogo:
```bash
python main.py
```
## Como jogar
1. No Menu Principal, pressione `1` para iniciar o expediente.
2. A cada rodada, você verá:
    - O valor da Compra e o Pagamento do cliente.
    - O Tempo Restante correndo (você tem 20 segundos!).
    - O Troco Alvo que deve ser devolvido.
3. Digite a quantidade necessária de cada moeda (começando pelas de maior valor, seguindo a lógica gulosa) e aperte `ENTER` para confirmar cada uma. Caso não precise adicionar `0` para uma nota, pode-se apenas apertar `ENTER` que preencherá automaticamente com `0`.
4. **Sistema de Pontuação:**
    - **Troco Perfeito** (Exato + Menos moedas possíveis): Pontuação máxima baseada no tempo de sobra.
    - **Troco Exato** (Porém usando moedas demais): Pontuação mínima.
    - **Troco Errado ou Tempo Esgotado:** Você perde pontos!
5. Você inicia com 100 pontos. Se a sua pontuação chegar a zero, a loja vai à falência.

*Projeto desenvolvido para a disciplina de Projeto de Algoritmos - 26.2*

