# Solução: Busca Binária

def busca_binaria(arr, x):
    esquerda = 0
    direita = len(arr) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(busca_binaria(arr, x))
