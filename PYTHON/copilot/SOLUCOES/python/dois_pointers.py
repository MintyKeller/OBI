# Solução: Dois Pointers (Two Sum II)

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

esquerda = 0
direita = n - 1

while esquerda < direita:
    soma = arr[esquerda] + arr[direita]
    
    if soma == target:
        print(esquerda + 1, direita + 1)  # 1-indexado
        break
    elif soma < target:
        esquerda += 1
    else:
        direita -= 1
