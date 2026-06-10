# r=resto, q=quociente
n = int(input())
resto = 2
q100= 0
q50 = 0
q20= 0
q10= 0
q5= 0
q2= 0
q1 = 0

#100
if (n%100)!= 0 : 
    q100= (n-(n%100))/100
elif (n%100) == 0:
    q100 = n/100

n = n - (q100*100)
#50
if (n%50)!=0:
    q50 = (n-(n%50))/50
elif (n%50) ==0: 
    q50 = n/50
n = n - (q50*50)
#20
if (n%20)!=0:
    q20 = (n-(n%20))/20
elif (n%20) ==0: 
    q20 = n/20
n = n - (q20*20)
#10
if (n%10)!=0:
    q10 = (n-(n%10))/10
elif (n%10) ==0: 
    q10 = n/10
n = n - (q10*10)
#5
if (n%5)!=0:
    q5 = (n-(n%5))/5
elif (n%5) ==0: 
    q5 = n/5
n = n - (q5*5)
#2
if (n%2)!=0:
    q2 = (n-(n%2))/2
elif (n%2) ==0: 
    q2 = n/2
n = n - (q2*2)
#1
if (n%1)!=0:
    q1 = (n-(n%1))/1
elif (n%1) ==0: 
    q1 = n/1
n = n - (q1*1)

q100= int(q100)
q50 = int(q50)
q20= int(q20)
q10= int(q10)
q5= int(q5)
q2= int(q2)
q1 = int(q1)


print(f"{q100} nota(s) de 100")
print(f"{q50} nota(s) de 50")
print(f"{q20} nota(s) de 20")
print(f"{q10} nota(s) de 10")
print(f"{q5} nota(s) de 5")
print(f"{q2} nota(s) de 2")
print(f"{q1} nota(s) de 1")

"""------------------COPILOT FEZ ASSIM----------------------"""
n = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = n // nota
    print(f"{quantidade} nota(s) de {nota}")
    n = n % nota


"""
    // = divisão inteira (sem decimal)
    / = divisão normal (com decimal)
    % = resto da divisão
    ** = potência"""



