salario_antigo = float(input())


def get_percentual(salario): 

    if 0<salario<=400.00: 
        percentual = 15/100
        return(percentual) 
    elif 400.01<=salario<=800.00: 
        percentual = 12/100
        return(percentual)
    elif 800.01<=salario<=1200.00: 
        percentual = 10/100
        return(percentual)
    elif 1200.01<=salario<=2000.00: 
        percentual = 7/100
        return(percentual)
    elif 2000.00<salario: 
        percentual = 4/100
        return(percentual)
    
percentual = get_percentual(salario_antigo)
print(percentual)

print(f"Novo salario: {salario_antigo +(salario_antigo*percentual)}")
print(f"Reajuste ganho: {(salario_antigo*percentual)}")
print(f"Em percentual: {int(percentual*100)}%")


