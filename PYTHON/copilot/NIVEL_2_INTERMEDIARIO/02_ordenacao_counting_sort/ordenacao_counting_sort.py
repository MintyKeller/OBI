quant = int(input)
numeros = list(map(int, input.split()))

ordenados = []
duplas = { }
duplas_ordenadas = {}

def get_index(number): 
    for i in range(quant): 
        if number ==  numeros[i]: 
            return(i); 

for i in range(quant): 
    a = numeros[i]
    a_index = get_index(a)
    nome = "dupla" + f"{i}"
    dictio = {
        "numero": a, 
        "index": a_index
    }
    duplas[f'{nome}'] = dictio


for a in range(quant): 
    for b in range(quant): 
        if a==b: 
            pass
        if numeros[a]< numeros[b]:
            if get_index(numeros[a])>get_index(numeros[b]): 
                a = numeros[a]
                b = numeros[b]
                index_a=get_index(numeros[a])
                index_b=get_index(numeros[b]) 
                while index_a>index_b: 
                   index_a = index_a - 1
                
