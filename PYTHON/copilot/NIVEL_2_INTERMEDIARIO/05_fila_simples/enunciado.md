# 05 - Fila (Queue) Simples

## Descrição

Simule uma **fila** com operações de enfileiramento (enqueue) e desenfileiramento (dequeue).

## Entrada

Primeira linha: um inteiro **N** (número de operações).
Próximas **N** linhas: operações no formato:
- `ENQUEUE X`: adiciona X no final da fila
- `DEQUEUE`: remove e printa o primeiro elemento
- `EMPTY`: printa 1 se vazia, 0 se não

## Saída

Resultado de cada operação (DEQUEUE e EMPTY).

## Exemplos

### Exemplo 1
**Entrada:**
```
6
ENQUEUE 10
ENQUEUE 20
DEQUEUE
DEQUEUE
EMPTY
ENQUEUE 5
```
**Saída:**
```
10
20
1
```

## Constraints

- `1 <= N <= 1000`

## Dicas

💡 **FIFO** (First In, First Out): O primeiro a entrar é o primeiro a sair.
💡 Use uma estrutura de dados de fila: `Queue` (Java), `deque` (Python), `queue<>` (C++).
