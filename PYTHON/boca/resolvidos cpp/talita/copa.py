k = int(input())
l = int(input())

def resultado(dif): 
    if dif == 1: 
        return("oitavas")
    elif dif == 2 or dif == 3: 
        return("quartas")
    elif dif == 4 or dif == 5 or dif == 6 or dif == 7: 
        return("semifinal")
    elif dif >=8: 
        return("final")


if k>l: 
    diferenca = k - l
    show = resultado(diferenca)
    print(show)
else: #k<l 
    diferenca = l - k
    show = resultado(diferenca)
    print(show)