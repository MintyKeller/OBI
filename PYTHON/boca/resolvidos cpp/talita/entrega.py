a = int(input())
b = int(input())
c = int(input())
#a<b<c 
if a == b and b == c and c == a: 
    print(3) 
elif (a+b) < c or (a+c) < b or (b+c)< a: 
    print(1)
elif  ((not((a+b) < c)) and (a<c or b<c)) or ((not((a+c) < b)) and (a<b or c<b)) or ((not((b+c) < a)) and (b<a or c<a)): 
    print(2)

"""
	            sort()	                    sorted()
Tipo	    Método (pertence a list)	Função built-in
Retorna	    Nada (modifica a lista)	    Nova lista ordenada
Usa	        lista.sort()	            sorted(lista)
Original	❌ Muda	                    ✅ Mantém
"""