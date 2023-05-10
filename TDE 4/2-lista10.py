contador = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while contador < len(numeros):
    contador += 1
    for i in numeros:
        print(f"{contador}  x  {i} = {contador * i}")
