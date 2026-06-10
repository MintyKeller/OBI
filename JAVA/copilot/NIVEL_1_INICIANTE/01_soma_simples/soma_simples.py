a, b = map(int, input().split()) 

if a < (-1000): 
    raise ValueError("O primeiro número não pode ser menor que -1000")
if b > 1000: 
    raise ValueError("O segundo número não pode ser maior que 1000")
    
print(a + b)