quant = int(input())
lista = list(map(int, input().split()))

aparecidos = ["x",]
for i in range(quant):
   if lista[i] not in aparecidos:
       aparecidos.append(lista[i])
   ''' for y in range(len(aparecidos)): 
        if lista[i] != aparecidos[y]: 
            aparecidos.append(lista[i])'''


aparecidos.remove("x")
nro = len(aparecidos)

contador = 0
for i in range(nro): 
    for y in range(quant):
        if aparecidos[i] == lista[y]:
            contador = contador +1 
    if contador == 1: 
        print(f"{aparecidos[i]} aparece {contador} vez")
    else:
        print(f"{aparecidos[i]} aparece {contador} vezes")
    contador = 0

"""------------------COPILOT COMPARISON------------------------"""
quant = int(input())
lista = list(map(int, input().split()))
aparecidos = []

for num in lista:
    if num not in aparecidos:
        aparecidos.append(num)

for num in aparecidos:
    freq = lista.count(num)
    if freq == 1:
        print(f"{num} aparece {freq} vez")
    else:
        print(f"{num} aparece {freq} vezes")
