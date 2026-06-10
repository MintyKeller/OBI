# 02 - Busca em Largura (BFS - Breadth First Search)

## Descrição

Implemente **BFS** para encontrar a distância mais curta entre dois pontos em um **labirinto**.

## Entrada

Primeira linha: **N** e **M** (dimensões do labirinto).
Próximas **N** linhas: o labirinto onde:
- `'.'` = célula livre
- `'#'` = parede

Última linha: posição inicial e final (startX, startY, endX, endY)

## Saída

A distância mais curta, ou `-1` se impossível.

## Exemplos

### Exemplo 1
**Entrada:**
```
3 3
. . .
# . #
. . .
0 0 2 2
```
**Saída:**
```
4
```

## Constraints

- `1 <= N, M <= 1000`

## Dicas

💡 Use uma **fila** para implementar BFS.
💡 Marque células visitadas para não revisitar.
💡 Explore 4 direções: cima, baixo, esquerda, direita.
