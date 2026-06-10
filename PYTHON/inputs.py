# Um número
numero = int(input())

# Dois números na mesma linha
a, b = map(int, input().split())

# Vários números na mesma linha
numeros = list(map(int, input().split()))

# Números em linhas diferentes
a = int(input())
b = int(input())
c = int(input())

"""------------------STRINGS-------------------------------"""
# Uma string
nome = input()

# Várias strings na mesma linha
nome1, nome2 = input().split()

# Múltiplas strings (como lista)
nomes = input().split()
"""---------------LISTA----------------------------------"""
# Lista de números
lista_nums = list(map(int, input().split()))

# Lista de strings
lista_strings = input().split()

# Lista vazia que você vai preenchendo depois
lista = []
for i in range(5):
    lista.append(int(input()))
"""---------------TUPLAS----------------------------------"""
# Tupla de números
tupla = tuple(map(int, input().split()))

# Tupla desempacotada direto
a, b, c = map(int, input().split())  # Isso já cria uma tupla implícita
"""----------------DICIONÁRIOS---------------------------------"""
# Dicionário simples (chave: valor)
dados = {}
chave = input()
valor = int(input())
dados[chave] = valor

# Ou criando direto
dados = {
    "nome": input(),
    "idade": int(input()),
    "altura": float(input())
}

# Dicionário com múltiplas entradas
dicionario = {}
n = int(input())
for i in range(n):
    chave, valor = input().split()
    dicionario[chave] = int(valor)
"""------------------FLOAT------------------------------"""
# Um float
numero = float(input())

# Vários floats
a, b = map(float, input().split())
"""---------------EXEMPLOS----------------------------------"""
# Problema típico: ler 2 números e somar
a, b = map(int, input().split())
print(a + b)

# Ler 3 números e fazer média
a, b, c = map(int, input().split())
media = (a + b + c) / 3
print(media)

# Ler N números e processar
n = int(input())
numeros = list(map(int, input().split()))
print(sum(numeros))
"""------------------RESUMO-------------------------------"""
# 1º - ler quantidade
n = int(input())

# 2º - ler dados (em loop ou tudo de uma vez)
dados = list(map(int, input().split()))

# 3º - processar
resultado = sum(dados)

# 4º - imprimir
print(resultado)