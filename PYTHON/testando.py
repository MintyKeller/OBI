S = input().lower()
frente = [c if c != "ç" else "c" for c in S if c != " "]
tras = frente[::-1]

if frente == tras:
    print("SIM")
else:
    print("NAO")