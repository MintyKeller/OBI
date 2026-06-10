# 03 - Greedy - Problema da Seleção de Atividades

## Descrição

Dado um conjunto de atividades com tempo de início e fim, selecione o **máximo número de atividades** que podem ser realizadas sem conflito (uma pessoa, um tempo).

## Entrada

Primeira linha: um inteiro **N** (quantidade de atividades).
Próximas **N** linhas: `inicio fim` de cada atividade.

## Saída

O número máximo de atividades que podem ser realizadas.

## Exemplos

### Exemplo 1
**Entrada:**
```
4
1 2
3 5
0 6
5 7
```
**Saída:**
```
2
```
(Atividades 0-6 e 7 sobrepõem, mas podemos fazer 1-2 e 3-5)

## Constraints

- `1 <= N <= 100000`

## Dicas

💡 **Greedy**: Ordene pela hora de término.
💡 Sempre escolha a atividade que termina mais cedo.
💡 Inclua próximas atividades que não conflitem.
