# 03 - Cédulas (Greedy Simples)

## Descrição

Faça um programa que leia um valor inteiro (em reais) e calcule o menor número de notas necessárias para representar esse valor.

Notas disponíveis: 100, 50, 20, 10, 5, 2, 1

## Entrada

Um inteiro **N** representando o valor em reais.

## Saída

7 linhas, mostrando quantas notas de cada denominação são necessárias.

## Exemplos

### Exemplo 1
**Entrada:**
```
576
```
**Saída:**
```
5 nota(s) de 100
1 nota(s) de 50
1 nota(s) de 20
0 nota(s) de 10
1 nota(s) de 5
0 nota(s) de 2
1 nota(s) de 1
```

### Exemplo 2
**Entrada:**
```
11
```
**Saída:**
```
0 nota(s) de 100
0 nota(s) de 50
0 nota(s) de 20
1 nota(s) de 10
0 nota(s) de 5
0 nota(s) de 2
1 nota(s) de 1
```

## Constraints

- `1 <= N <= 1000000`

## Dicas

💡 **Greedy Algorithm**: Use a maior nota possível primeiro, depois siga para as menores.
💡 Use divisão inteira (`//` ou `/`) e módulo (`%`) para calcular.
