# Solução: Fila Simples

from collections import deque

fila = deque()
n = int(input())

for _ in range(n):
    operacao = input().split()
    
    if operacao[0] == "ENQUEUE":
        valor = int(operacao[1])
        fila.append(valor)
    elif operacao[0] == "DEQUEUE":
        if fila:
            print(fila.popleft())
    elif operacao[0] == "EMPTY":
        if len(fila) == 0:
            print(1)
        else:
            print(0)
