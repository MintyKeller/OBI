# 04 - Palíndromo

## Descrição

Um palíndromo é uma palavra ou frase que é lida da mesma forma de trás para frente (ignorando espaços e maiúsculas/minúsculas).

Verifique se uma string é um palíndromo.

## Entrada

Uma string **S** contendo apenas letras e espaços.

## Saída

Printe `"SIM"` se for palíndromo, `"NAO"` caso contrário.

## Exemplos

### Exemplo 1
**Entrada:**
```
raça a car
```
**Saída:**
```
SIM
```

### Exemplo 2
**Entrada:**
```
aba
```
**Saída:**
```
SIM
```

### Exemplo 3
**Entrada:**
```
hello
```
**Saída:**
```
NAO
```

## Constraints

- `1 <= |S| <= 1000`

## Dicas

💡 Remova os espaços da string.
💡 Converta para minúsculas.
💡 Compare com sua versão invertida.
