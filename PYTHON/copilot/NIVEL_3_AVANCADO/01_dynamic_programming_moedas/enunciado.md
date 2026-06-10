# 01 - Dynamic Programming - Problema das Moedas

## Descrição

Dado um conjunto de moedas de valores diferentes, encontre o **número mínimo de moedas** necessárias para atingir um valor **N**.

## Entrada

Primeira linha: um inteiro **N** (valor alvo) e **M** (quantidade de tipos de moedas).
Segunda linha: **M** inteiros (valores das moedas).

## Saída

O número mínimo de moedas para formar o valor **N**, ou `-1` se impossível.

## Exemplos

### Exemplo 1
**Entrada:**
```
11 3
1 5 6
```
**Saída:**
```
3
```
(Usar 5 + 5 + 1 = 3 moedas)

### Exemplo 2
**Entrada:**
```
5 2
2 4
```
**Saída:**
```
-1
```
(Impossível formar 5 com moedas de 2 e 4)

## Constraints

- `1 <= N <= 10000`
- `1 <= M <= 100`

## Dicas

💡 **DP[i]** = número mínimo de moedas para formar o valor `i`.
💡 `DP[0] = 0` (base)
💡 `DP[i] = min(DP[i - moeda] + 1)` para cada moeda válida.
