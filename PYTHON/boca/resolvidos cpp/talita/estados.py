estado = input()
regiao_norte = ["roraima", "acre", "amapa", "amazonas", "para","rondonia", "tocantins"]

contador = 0

for est in regiao_norte: 
    if est == estado: 
        print("Regiao Norte") 
    else: 
        contador = contador + 1 

if contador == 7: 
    print("Outra regiao")



"""
python tem break!!!         break  # Para o loop!
"""

"""-----------------------versao COPILOT--------------------------------------"""
estado = input()
regiao_norte = ["roraima", "acre", "amapa", "amazonas", "para", "rondonia", "tocantins"]

if estado in regiao_norte:
    print("Regiao Norte")
else:
    print("Outra regiao")
