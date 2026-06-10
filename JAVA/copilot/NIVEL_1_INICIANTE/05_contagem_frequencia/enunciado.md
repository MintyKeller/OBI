# 05 - Contagem de Frequência

## Descrição

Dado um array de números, conte quantas vezes cada número aparece.

## Entrada

Primeira linha: um inteiro **N** (quantidade de elementos).
Segunda linha: **N** inteiros separados por espaço.

## Saída

Para cada número único (em ordem de aparição), imprima o número e sua frequência.

## Exemplos

### Exemplo 1
**Entrada:**
```
5
1 2 1 3 2
```
**Saída:**
```
1 aparece 2 vezes
2 aparece 2 vezes
3 aparece 1 vez
```

### Exemplo 2
**Entrada:**
```
4
5 5 5 5
```
**Saída:**
```
5 aparece 4 vezes
```

## Constraints

- `1 <= N <= 1000`
- `1 <= números <= 100`

## Dicas

💡 Use um **dicionário** ou **HashMap** para contar frequências.
💡 Mantenha a ordem de primeiro aparecimento.
