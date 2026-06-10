# 02 - Ordenação (Counting Sort)

## Descrição

Ordene um array de números. Para valores em um intervalo limitado, use **Counting Sort** (O(n+k)).

## Entrada

Primeira linha: um inteiro **N** (quantidade de elementos).
Segunda linha: **N** inteiros separados por espaço.

## Saída

Os **N** números em ordem crescente.

## Exemplos

### Exemplo 1
**Entrada:**
```
5
3 1 4 1 5
```
**Saída:**
```
1 1 3 4 5
```

### Exemplo 2
**Entrada:**
```
6
10 5 8 5 10 3
```
**Saída:**
```
3 5 5 8 10 10
```

## Constraints

- `1 <= N <= 100000`
- `0 <= números <= 1000`

## Dicas

💡 **Counting Sort**: Crie um array `count` onde `count[i]` = quantas vezes `i` aparece.
💡 Percorra esse array e reconstrua o resultado ordenado.
💡 Complexidade: O(n + k), onde k é o intervalo de valores.
