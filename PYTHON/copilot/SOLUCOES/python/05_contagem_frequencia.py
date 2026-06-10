# Solução: Contagem de Frequência

from collections import OrderedDict

n = int(input())
numeros = list(map(int, input().split()))

freq = {}
for num in numeros:
    if num not in freq:
        freq[num] = 0
    freq[num] += 1

for num in freq:
    if freq[num] == 1:
        print(f"{num} aparece 1 vez")
    else:
        print(f"{num} aparece {freq[num]} vezes")
