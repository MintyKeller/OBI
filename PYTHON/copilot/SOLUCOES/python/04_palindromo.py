# Solução: Palíndromo

s = input().lower().replace(" ", "")

if s == s[::-1]:
    print("SIM")
else:
    print("NAO")
