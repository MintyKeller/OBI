# 01 - Busca Binária

## Descrição

Implemente uma busca binária em um array **já ordenado**. Retorne o índice do elemento se encontrado, ou `-1` se não existir.

## Entrada

Primeira linha: um inteiro **N** (quantidade de elementos).
Segunda linha: **N** inteiros ordenados separados por espaço.
Terceira linha: um inteiro **X** (o número a buscar).

## Saída

O índice de **X** no array (começando em 0), ou `-1` se não encontrado.

## Exemplos

### Exemplo 1
**Entrada:**
```
5
1 3 5 7 9
5
```
**Saída:**
```
2
```

### Exemplo 2
**Entrada:**
```
5
1 3 5 7 9
4
```
**Saída:**
```
-1
```

### Exemplo 3
**Entrada:**
```
6
10 20 30 40 50 60
10
```
**Saída:**
```
0
```

## Constraints

- `1 <= N <= 100000`
- `-1000000 <= elementos <= 1000000`

## Dicas

💡 **Complexidade**: O(log N) - muito mais rápido que busca linear!
💡 Mantenha dois ponteiros: `esquerda` e `direita`.
💡 A cada iteração, divida o intervalo de busca pela metade.
