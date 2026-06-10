S = input().lower()
frente = []

for i in range(len(S)): 
    if(S[i]==" "):
        pass
    elif S[i]=="ç": 
        frente.append("c")
    else:
        frente.append(S[i])
    

tras = []
nro = len(frente)

for i in range(nro, 0, -1):
   char = frente[i-1]
   tras.append(char)

contador = 0
for i in range(len(frente)):
    if frente[i] == tras[i]:
        contador = contador +1

if contador == len(frente): 
    print("SIM")
else: 
    print("NAO")
   

"""--------------------COPILOT--------------------------"""
S = input().lower()
frente = [c if c != "ç" else "c" for c in S if c != " "]
tras = frente[::-1]

if frente == tras:
    print("SIM")
else:
    print("NAO")