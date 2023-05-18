import random

numSorteados = random.sample(range(10, 100), 105)
count = 0
matriz = []
for i in range(15):
    linha = []
    for j in range(7):
            linha.append(numSorteados[count])
            count += 1
    matriz.append(linha)


print(matriz)