# 03 - Soma de Subarray Máximo (Kadane's Algorithm)

## Descrição

Encontre a soma máxima de um **subarray contíguo** (Algoritmo de Kadane).

## Entrada

Primeira linha: um inteiro **N**.
Segunda linha: **N** inteiros.

## Saída

A soma máxima possível de um subarray contíguo.

## Exemplos

### Exemplo 1
**Entrada:**
```
5
-2 1 -3 4 -1
```
**Saída:**
```
4
```
(Subarray: [4])

### Exemplo 2
**Entrada:**
```
6
5 -3 5 -2 8 -1
```
**Saída:**
```
15
```
(Subarray: [5, -3, 5, -2, 8])

### Exemplo 3
**Entrada:**
```
4
-1 -2 -3 -4
```
**Saída:**
```
-1
```

## Constraints

- `1 <= N <= 100000`
- `-10000 <= números <= 10000`

## Dicas

💡 **Kadane's Algorithm**: Para cada posição, decida se continua o subarray anterior ou começa um novo.
💡 `max_ending_here = max(elemento, max_ending_here + elemento)`
💡 Complexidade: O(n)
