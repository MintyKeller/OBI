# 04 - Dois Ponteiros (Two Sum II)

## Descrição

Dado um array **ordenado**, encontre dois números cuja soma seja igual a um alvo **target**.

## Entrada

Primeira linha: um inteiro **N**.
Segunda linha: **N** inteiros ordenados.
Terceira linha: um inteiro **TARGET**.

## Saída

Os índices dos dois números (1-indexado, ou seja, começando em 1).

## Exemplos

### Exemplo 1
**Entrada:**
```
4
2 7 11 15
9
```
**Saída:**
```
1 2
```
(números 2 e 7, índices 1 e 2)

### Exemplo 2
**Entrada:**
```
5
1 2 3 4 5
8
```
**Saída:**
```
3 5
```
(números 3 e 5, índices 3 e 5)

## Constraints

- `2 <= N <= 100000`
- Array está ordenado
- Sempre existe solução

## Dicas

💡 Use **dois ponteiros**: um no início (`esquerda`) e outro no fim (`direita`).
💡 Se soma < target, mova esquerda para direita.
💡 Se soma > target, mova direita para esquerda.
💡 Complexidade: O(n)
