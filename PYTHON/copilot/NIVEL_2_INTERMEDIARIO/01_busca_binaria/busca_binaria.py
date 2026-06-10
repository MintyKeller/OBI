quant = int(input())
array = list(map(int, input().split()))
procurado = int(input())

for i in range(quant): 
   if procurado == array[i]: 
      print(i)

if procurado  not in array: 
    print((-1))